// var dom=document.getElementById("box3_left");
// var myChart=echarts.init(dom);
// var app={};
// option=null;
// app.title="极坐标系下的堆叠柱状图";
// option={textStyle:{color:"#dbdbdb",fontSize:10},angleAxis:{},radiusAxis:{type:"category",data:["周一","周二","周三","周四"],z:10},polar:{},series:[{type:"bar",data:[1,2,3,4],coordinateSystem:"polar",name:"A",stack:"a"},{type:"bar",data:[2,4,6,8],coordinateSystem:"polar",name:"B",stack:"a"},{type:"bar",data:[1,2,3,4],coordinateSystem:"polar",name:"C",stack:"a"}],legend:{show:true,textStyle:{color:"#dbdbdb",fontSize:10},data:["A","B","C"]}};if(option&&typeof option==="object"){myChart.setOption(option,true)};
//
var chart1 = echarts.init(document.getElementById('box3_left'), 'ESSOS', {renderer: 'canvas'});
                $.ajax({
                    type: "GET",
                    url: "http://127.0.0.1:5000/polarChart",
                    dataType: 'json',
                    success: function (result) {
                        chart1.setOption(result);
                    }
                     });