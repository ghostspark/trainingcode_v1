var dom=document.getElementById("box1");
var myChart=echarts.init(dom);
var app={};option=null;
    var labelRight={normal:{position:"right"}};
    option={
        tooltip:{trigger:"axis",axisPointer:{type:"shadow"}},
        grid:{left:10,top:20,bottom:30},
        xAxis:{type:"value",position:"top",splitLine:{lineStyle:{type:"dashed"}},},
        textStyle:{color:"#fff",fontSize:12},
        yAxis:{type:"category",axisLine:{show:false},axisLabel:{show:false},axisTick:{show:false},splitLine:{show:false},data:["ten","nine","eight","seven","six","five","four","three","two","one"]},
        series:[{name:"生活费",type:"bar",stack:"总量",label:{normal:{show:true,formatter:"{b}"}},
            data:[{value:-0.07000000000000001,label:labelRight},{value:-0.09,label:labelRight},0.2,0.44,{value:-0.23,label:labelRight},0.08,{value:-0.17,label:labelRight},0.47,{value:-0.36,label:labelRight},0.18]}]
    };
    if(option&&typeof option==="object"){myChart.setOption(option,true)};












