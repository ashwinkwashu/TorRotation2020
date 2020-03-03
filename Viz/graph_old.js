// w=12000
// h = 1000

// var svg = d3.select('body')
// .append('svg')
// .attr('id','graph')
// .attr('viewBox', '0 0 ' + w + ' ' + h);

// svg.append('circle').attr('cx', 100).attr('cy', 100).attr('r', 100);


var color = d3.scaleOrdinal(d3.schemeCategory10)

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
function get_data(){
    d3.json('v2_json_dump.json',function (data){
            v2_data = data;
            // console.log(v2_data);
            v2_data.forEach(function(d,i){

            // The number of datapoints
            var n = d.data.length + 2;
            
            console.log(n)

            // 5. X scale will use the index of our data
            var xScale = d3.scaleLinear()
                .domain([0, n-1]) // input
                .range([0, width]); // output

            // 6. Y scale will use the randomly generate number 
            var yScale = d3.scaleLinear()
                .domain([0, 250]) // input 
                .range([height/2, 0]); // output 

            // 7. d3's line generator
            var line = d3.line()
                .x(function(d, i) { return xScale(i) }) // set the x values for the line generator
                .y(function(d) { return yScale(+d.y); }) // set the y values for the line generator 
                .curve(d3.curveMonotoneX) // apply smoothing to the line

            // 8. An array of objects of length N. Each object has key -> value pair, the key being "y" and the value is a random number
            var dataset = d.data;
            console.log(dataset)

            dataset.unshift({'y':0});
            dataset.push({'y':0});

            if(flag ===1){
                // 1. Add the SVG to the page and employ #2
                var points = d3.select("body").append("svg")
                    .attr('id','graph')
                    .attr("width", width + margin.left + margin.right)
                    .attr("height", height + margin.top + margin.bottom)
                .append("g")
                    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

                // 3. Call the x axis in a group tag
                points.append("g")
                    .attr("class", "x axis")
                    .attr("transform", "translate(0," + height/2 + ")")
                    .call(d3.axisBottom(xScale)); // Create an axis component with d3.axisBottom

                // 4. Call the y axis in a group tag
                points.append("g")
                    .attr("class", "y axis")
                    .call(d3.axisLeft(yScale)); // Create an axis component with d3.axisLeft
                
                    flag =0;
                    // 9. Append the path, bind the data, and call the line generator 
                    points.append("path")
                    .datum(dataset) // 10. Binds data to the line 
                    .attr("class", "line") // Assign a class for styling 
                    .attr("d", line) // 11. Calls the line generator 
                    .attr('fill','blue')
                    .attr('stroke', 'black')

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
                    .x(function(d, i) { return xScale(i) + margin.left; }) // set the x values for the line generator
                    .y(function(d) { return yScale(+d.y) + margin.top; }) // set the y values for the line generator 
                    .curve(d3.curveMonotoneX) // apply smoothing to the line
                points = d3.select("#graph");
                // 9. Append the path, bind the data, and call the line generator 
                points.append("path")
                .datum(dataset) // 10. Binds data to the line 
                .attr("class", "line") // Assign a class for styling 
                .attr("d", line) // 11. Calls the line generator 
                .attr('fill',color(i%10))
                .attr('stroke', 'black')
                .on('mouseover', function(d){

                })

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
get_data();
