//https://bl.ocks.org/gordlea/27370d1eea8464b04538e6d8ced39e89

// w=12000
// h = 1000

// var svg = d3.select('body')
// .append('svg')
// .attr('id','graph')
// .attr('viewBox', '0 0 ' + w + ' ' + h);

// svg.append('circle').attr('cx', 100).attr('cy', 100).attr('r', 100);


var color = d3.scaleOrdinal(d3.schemeCategory20)
// var color = d3.scaleOrdinal(d3.schemeTableau10)
// var color= d3.scaleSequential(d3.interpolateRdYlBu);
// var color= d3.scaleSequential(d3.interpolateTurbo);
console.log(color)
console.log(color(1))
// var color = d3.scaleOrdinal(d3.schemeTableau10)
//methods and variables for the tooltip
var div = d3.select("body").append("div")	
    .attr("class", "tooltip")				
    .style("opacity", 0);

//Fade in for the tooltip
function tooltip_in(d){
    //show the tooltip
    div.transition()		
        .duration(200)		
        .style("opacity", .9);		
    div.html(d)	
        .style("left", (d3.event.pageX + 20) + "px")		
        .style("top", (d3.event.pageY - 50) + "px");
}

//fade out for the tooltip
function tooltip_out(d) {		
    div.transition()		
        .duration(500)		
        .style("opacity", 0);
}

// 2. Use the margin convention practice 
var margin = {top: 50, right: 50, bottom: 50, left: 50}
  , width = window.innerWidth - margin.left - margin.right // Use the window's width 
  , height = window.innerHeight - margin.top - margin.bottom; // Use the window's height

// // The number of datapoints
// var n = 21;

// // 5. X scale will use the index of our data
// var xScale = d3.scaleLinear()
//     .domain([0, n-1]) // input
//     .range([0, width]); // output

// // 6. Y scale will use the randomly generate number 
// var yScale = d3.scaleLinear()
//     .domain([0, 1]) // input 
//     .range([height, 0]); // output 

// // 7. d3's line generator
// var line = d3.line()
//     .x(function(d, i) { return xScale(i); }) // set the x values for the line generator
//     .y(function(d) { return yScale(d.y); }) // set the y values for the line generator 
//     .curve(d3.curveMonotoneX) // apply smoothing to the line

// // 8. An array of objects of length N. Each object has key -> value pair, the key being "y" and the value is a random number
// var dataset = d3.range(n-2).map(function(d) { return {"y": d3.randomUniform(1)() } })

// dataset.unshift({'y':0});
// dataset.push({'y':0});


// // 1. Add the SVG to the page and employ #2
// var svg = d3.select("body").append("svg")
//     .attr("width", width + margin.left + margin.right)
//     .attr("height", height + margin.top + margin.bottom)
//   .append("g")
//     .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// // 3. Call the x axis in a group tag
// svg.append("g")
//     .attr("class", "x axis")
//     .attr("transform", "translate(0," + height + ")")
//     .call(d3.axisBottom(xScale)); // Create an axis component with d3.axisBottom

// // 4. Call the y axis in a group tag
// svg.append("g")
//     .attr("class", "y axis")
//     .call(d3.axisLeft(yScale)); // Create an axis component with d3.axisLeft

// // 9. Append the path, bind the data, and call the line generator 
// svg.append("path")
//     .datum(dataset) // 10. Binds data to the line 
//     .attr("class", "line") // Assign a class for styling 
//     .attr("d", line) // 11. Calls the line generator 
//     .attr('fill','none')
//     .attr('stroke', 'black')

// // 12. Appends a circle for each datapoint 
// svg.selectAll(".dot")
//     .data(dataset)
//   .enter().append("circle") // Uses the enter().append() method
//     .attr("class", "dot") // Assign a class for styling
//     .attr("cx", function(d, i) { return xScale(i) })
//     .attr("cy", function(d) { return yScale(d.y) })
//     .attr("r", 5)
//       .on("mouseover", function(a, b, c) { 
//   			console.log(a) 
//         this.attr('class', 'focus')
// 		})



var v2_data = []
var flag = 1;
var h_scale = 1;
function get_data(filename){
    d3.json(filename,function (data){
            flag = 1;
        
            v2_data = data;
            // console.log(v2_data);
            data.forEach(function(d,i){

            // The number of datapoints
            var n = d.data.length + 2;
            var time = d.time;
            var counts = d.counts;
            // console.log(n)

            // 5. X scale will use the index of our data
            var xScale =  d3.scaleTime()
            // d3.scaleLinear()
                .domain([Date.parse(d.data[0].x), Date.parse(d.data[n-3].x)]) // input
                .range([0, width*h_scale]); // output

            // 6. Y scale will use the randomly generate number 
            var yScale = d3.scaleLinear()
                .domain([0, 250]) // input 
                .range([1.8*height/3, height/10]); // output 

            // 7. d3's line generator
            var line = d3.line()
                .x(function(d, i) {
                    //  console.log(xScale(+Date.parse(d.x)), d);
                     return xScale(+Date.parse(d.x)) }) // set the x values for the line generator
                .y(function(d) { return yScale(+d.y); }) // set the y values for the line generator 
                // .curve(d3.curveMonotoneX) // apply smoothing to the line

            // 8. An array of objects of length N. Each object has key -> value pair, the key being "y" and the value is a random number
            var dataset = d.data;
            // console.log(dataset)

            dataset.unshift({'x':d.data[0].x ,'y':0}); //push x as d[0].x
            dataset.push({'x': d.data[n-2].x,'y':0});

            if(flag ===1){
                console.log(filename)
                // 1. Add the SVG to the page and employ #2
                var points = d3.select("body").append("svg")
                    // .style("overflow-x","scroll")
                    .attr('id','graph'.concat(filename.slice(0,10)))
                    .attr("width", width*h_scale + margin.left + margin.right)
                    .attr("height", 2*height/3 + margin.top + margin.bottom)
                .append("g")
                    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

                // 3. Call the x axis in a group tag
                points.append("g")
                    .attr("class", "x axis")
                    .attr("transform", "translate(0," + 1.8*height/3 + ")")
                    // .ticks(d3.timeMinute.every(15))
                    .call(d3.axisBottom(xScale)
                        .ticks(d3.timeHour.every(12))
                    ); // Create an axis component with d3.axisBottom
             
                // 4. Call the y axis in a group tag
                points.append("g")
                    .attr("class", "y axis")
                    .call(d3.axisLeft(yScale)); // Create an axis component with d3.axisLeft
                
                    flag =0;
                    // 9. Append the path, bind the data, and call the line generator 
                    // points.append("path")
                    // .datum(dataset) // 10. Binds data to the line 
                    // .attr("class", "line") // Assign a class for styling 
                    // .attr("d", line) // 11. Calls the line generator 
                    // .attr('fill','blue')
                    // .attr('stroke', 'black')
                points.append("text")
                    .attr("x", (width / 2))             
                    .attr("y", 0 + (margin.top))
                    .attr("text-anchor", "middle")  
                    .style("font-size", "16px") 
                    // .style("text-decoration", "underline") 
                    .text("Descriptor count vs Date ("+filename.slice(0,-15)+')');
                // // 12. Appends a circle for each datapoint 
                // points.selectAll(".dot")
                //     .data(dataset)
                // .enter().append("circle") // Uses the enter().append() method
                //     .attr("class", "dot") // Assign a class for styling
                //     .attr("cx", function(d, i) { return xScale(i) })
                //     .attr("cy", function(d) { return yScale(d.y) })
                //     .attr("r", 5)
                //     .on("mouseover", function(a, b, c) { 
                //             console.log(a) 
                //         this.attr('class', 'focus')
                //         })
                
            };
            if (flag ==0){
                var line = d3.line()
                    .x(function(d, i) { return xScale(Date.parse(d.x)) + margin.left; }) // set the x values for the line generator
                    .y(function(d) { return yScale(+d.y) + margin.top; }) // set the y values for the line generator 
                    .curve(d3.curveMonotoneX) // apply smoothing to the line
                    // .curve(d3.curveLinear);
                points = d3.select("#graph".concat(filename.slice(0,10)));
                // 9. Append the path, bind the data, and call the line generator 
                points.append("path")
                .datum(dataset) // 10. Binds data to the line 
                .attr("class", "line") // Assign a class for styling 
                .attr("d", line) // 11. Calls the line generator 
                .attr('fill', function(d){
                    return color(i%10);
                    return color(i/n);
                })
                .attr('stroke', function(d){
                    return color(i%10);
                    return color(i/n);
                })
                // .attr('time')
                .on('mouseover', function(d){
                     //show the duration of stay on hover
                // console.log('Mouse')    
                var pathtime = time;
                points.selectAll(".dot").remove();
                points.selectAll(".dot")
                    .data(dataset)
                .enter().append("circle") // Uses the enter().append() method
                    .attr("class", "dot") // Assign a class for styling
                    .attr("cx", function(d, i) { val = xScale(Date.parse(d.x)); return val + margin.left; })
                    .attr('time', function(d){ 
                        if (d.x == pathtime){
                            points.selectAll('line').remove();
                            points.append('line')
                                .attr('x1',xScale(+Date.parse(d.x)) + margin.left)
                                .attr('x2', xScale(+Date.parse(d.x)) + margin.left)
                                .attr('y1', yScale(0) + margin.top)
                                .attr('y2', yScale(d.y) + margin.top)
                                .attr('stroke', 'black')
                                .attr('stroke-width',4)

                        };
                        return d.x})
                    .attr("cy", function(d) { return yScale(d.y) + margin.top})
                    .attr('count', function(d){ return d.y})
                    .attr("r", 4)
                    .on("mouseover", function(d) { 
                        d3.select(this).transition().attr('r', 6 );
                        // console.log(d3.select(this))
                        prnt = d3.select(this).attr('time') + "<br/>" + d3.select(this).attr('count');
                        return tooltip_in(prnt)

                                })
                    .on('mouseout', function(d) {
                        d3.select(this).attr('r',4);
                        return tooltip_out(d)
                    })
                    prnt = time + "<br/>" + counts;
                    return tooltip_in(prnt)
                })
                .on("mouseout", function(d){return tooltip_out(d)});;

                // // 12. Appends a circle for each datapoint 
                // points.selectAll(".dot")
                //     .data(dataset)
                // .enter().append("circle") // Uses the enter().append() method
                //     .attr("class", "dot") // Assign a class for styling
                //     .attr("cx", function(d, i) { val = xScale(i); return val; })
                //     .attr("cy", function(d) { return yScale(d.y)})
                //     .attr("r", 5)
                //     .on("mouseover", function(a, b, c) { 
                //             console.log(a) 
                //         this.attr('class', 'focus')
                //         })
            }

            

                
            })
        })
    }
get_data('v2_json_dump.json');
get_data('v2_replicas_json_dump.json');
get_data('v2_uniques_json_dump.json');
get_data('v3_json_dump.json');
get_data('v3_replicas_json_dump.json');
get_data('v3_uniques_json_dump.json');
//v2/v3: descriptors which were common across the two files by the selected field (ed25519 cert-v3, permanent key - v2)
//replicas: descriptors which were there in the other file (common), and have 2 fields exactly matching
//uniques: descriptors that were in the other file (common) but are not replicas
