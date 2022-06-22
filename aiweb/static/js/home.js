$('#add_con').click(function(){
    const city1 =document.getElementById('city1').value
    const city2 =document.getElementById('city2').value
    const connect =document.getElementById('connect').value
     $.ajax({
         url:'',
         type:'get',
         data:{
             'add_con':'add_con',
             'city1': city1,
             'city2': city2
            ,'connect':connect
         },
     }
     )   
     document.getElementById('city1').value=''
     document.getElementById('city2').value=''
     document.getElementById('connect').value='' 
 }
 );
$('#add_inf').click(function(){
     const city_inf =document.getElementById('city_inf').value
     const Inference =document.getElementById('Inference').value
     $.ajax({
         url:'',
         type:'get',
         data:{
             'add_inf' :'add_inf',
              'city_inf': city_inf,
              'Inference': Inference
         },
     }
     )
     document.getElementById('city_inf').value=''
     document.getElementById('Inference').value='' 
 }
 );
$('#showbtn').click(function(){
     const start =document.getElementById('start').value
     const end =document.getElementById('end').value
     console.log("showbtn")
     $.ajax({
         url:'',
         type:'get',
         data:{
             'showbtn' :'showbtn',
              'start': start,
              'end': end
         },
          success:function(response){
             document.getElementById('path_out').value=response.result
         }
     }
     )
     document.getElementById('start').value=''
     document.getElementById('end').value='' 
 }
 ); 
