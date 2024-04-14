// var dom=document.getElementById("box4");var myChart=echarts.init(dom);var app={};option=null;option={legend:{textStyle:{color:"#fff",fontSize:12},data:["图一","图二","张三","李四"]},radar:[{indicator:[{text:"指标一"},{text:"指标二"},{text:"指标三"},{text:"指标四"},{text:"指标五"}],center:["25%","50%"],radius:120,startAngle:90,splitNumber:4,shape:"circle",name:{formatter:"【{value}】",textStyle:{color:"#72ACD1"}},splitArea:{areaStyle:{color:["rgba(114, 172, 209, 0.2)","rgba(114, 172, 209, 0.4)","rgba(114, 172, 209, 0.6)","rgba(114, 172, 209, 0.8)","rgba(114, 172, 209, 1)"],shadowColor:"rgba(0, 0, 0, 0.3)",shadowBlur:10}},axisLine:{lineStyle:{color:"rgba(255, 255, 255, 0.5)"}},splitLine:{lineStyle:{color:"rgba(255, 255, 255, 0.5)"}}},{indicator:[{text:"参数一",max:150},{text:"参数二",max:150},{text:"参数三",max:150},{text:"参数四",max:120},{text:"参数五",max:108},{text:"参数六",max:72}],center:["75%","50%"],radius:120}],series:[{name:"雷达图",type:"radar",itemStyle:{emphasis:{lineStyle:{width:4}}},data:[{value:[100,8,0.4,-80,2000],name:"图一",symbol:"rect",symbolSize:5,lineStyle:{normal:{type:"dashed"}}},{value:[60,5,0.3,-100,1500],name:"图二",areaStyle:{normal:{color:"rgba(255, 255, 255, 0.5)"}}}]},{name:"成绩单",type:"radar",radarIndex:1,data:[{value:[120,118,130,100,99,70],name:"张三",label:{normal:{show:true,formatter:function(a){return a.value}}}},{value:[90,113,140,30,70,60],name:"李四",areaStyle:{normal:{opacity:0.9,color:new echarts.graphic.RadialGradient(0.5,0.5,1,[{color:"#B8D3E4",offset:0},{color:"#72ACD1",offset:1}])}}}]}]};if(option&&typeof option==="object"){myChart.setOption(option,true)};

var chart2 = echarts.init(document.getElementById('box4'), 'ESSOS', {renderer: 'canvas'});
                $.ajax({
                    type: "GET",
                    url: "http://127.0.0.1:5000/barChart",
                    dataType: 'json',
                    success: function (result) {
                        chart2.setOption(result);
                    }
                     });