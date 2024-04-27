fetch('http://127.0.0.1:3766/api/v1/get-users-by-age')
  .then(response => response.json())
  .then(data => {
    createBarChartAge(data.data);
  })
  .catch(error => console.error('Error fetching data:', error));

function createBarChartAge(data) {
  const svgWidth = 800;
  const svgHeight = 400;
  const margin = { top: 20, right: 20, bottom: 80, left: 90 };
  const width = svgWidth - margin.left - margin.right;
  const height = svgHeight - margin.top - margin.bottom;

  const svg = d3.select("#age_chart")
      .append("svg")
      .attr("width", svgWidth)
      .attr("height", svgHeight)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  const xScale = d3.scaleBand()
      .domain(data.map(d => d.age_group))
      .range([0, width])
      .padding(0.1);

  const yScale = d3.scaleLinear()
      .domain([0, d3.max(data, d => d.total_users)])
      .nice()
      .range([height, 0]);

  svg.selectAll(".bar")
      .data(data)
      .enter()
      .append("rect")
      .attr("class", "bar")
      .attr("x", d => xScale(d.age_group))
      .attr("y", height) 
      .attr("width", xScale.bandwidth())
      .attr("height", 0)
      .transition() 
      .duration(1000) 
      .attr("y", d => yScale(d.total_users))
      .attr("height", d => height - yScale(d.total_users));

  svg.append("g")
      .attr("class", "axis-x")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(xScale))
      .selectAll("text")
      .attr("transform", "rotate(-45)")
      .style("text-anchor", "end");

  svg.append("g")
      .attr("class", "axis-y")
      .call(d3.axisLeft(yScale));
}
