createDB();




function updateIndicator() {
    if(navigator.onLine)
      {
  
      document.getElementById("status_alert").className = "alert alert-success ";
      document.getElementById('status_alert').innerHTML="Online";
      transferElement();
    }
    else {
       document.getElementById('status_alert').innerHTML="Offline"
       document.getElementById("status_alert").className = "alert alert-danger";
  
    }
    console.log(navigator.onLine)
  
  }
  

  function submitPress()
  {
    console.log('submitted');
    addElement();
    

    if(navigator.onLine)
    {
      transferElement();
    }
  }



function addElement()
{
    var tx=db.transaction("booking_table","readwrite");
    var tab=tx.objectStore('booking_table');    
    var name=document.getElementById("name").value;
    var adults=document.getElementById("adults").value;
    var mobile=document.getElementById("mobile").value;
    var children=document.getElementById("children").value;
    var email=document.getElementById("email").value;
    var arrival_date=document.getElementById("arrdate").value;
    var depdate=document.getElementById("depdate").value;
    var rooms=document.getElementById("rooms").value;

    

    const obj={'name':name,'depdate':depdate, 'adults': adults,'mobile':mobile,'children':childern,'email':email,'arrdate':arrdate,'rooms': rooms};

    tab.add(obj);
    //btnPressChk=-1;

    
}


function createDB()
{
    var req=indexedDB.open("travelDb",1);

    req.onsuccess=(a)=>{
        //console.log("sucess")
        //console.log(a.target)
        db=a.target.result
        

    }

    req.onupgradeneeded=function(u)
    {
        console.log('upgraded');
        db=u.target.result
        var tab=db.createObjectStore('booking_table',{keyPath:"name"});
        
        //tab.createIndex('name','name',{uniqe:true});
        

        
        
    }

    req.onerror=function(e)
    {
        console.log('error:'+e.target.error);
        
    }   
    
}


function transferElement()
{
    console.log('called')
    const tx = db.transaction("booking_table","readwrite")
    const ptab = tx.objectStore("booking_table")
    const request = ptab.openCursor()
    var xhttp=new XMLHttpRequest();


    request.onsuccess = function(e){
        const cursor = e.target.result
        
        
            if (cursor) 
            {
                //do something with the cursor
                var name=cursor.value.name;
                xhttp.onreadystatechange=function()
                {
                    if(this.status==200 && this.readyState==4)
                        {console.log(this.responseText);
                        alert('Sent to server!');
                        if(xhttp.responseText=='done')
                            {   
                                popElement();
                                document.getElementById('transfer').click();
                                
                            }
                        
                    }
                    else 
                        console.log(`Status:${this.status} Ready state:${this.readyState}`);
                    }
                    
                    var json=JSON.stringify(cursor.value);
                    //console.log(cursor);
                    console.log(json);
                    xhttp.open("POST",'http://localhost:5000/transfer',true);
                    console.log('Sending'+json);
                    xhttp.send(json);

                    console.log('Recieved'+ xhttp.responseText);
                    

                
            }
        }   

    

    /*request.onerror= e =>{
        console.log('Error:'+e.target.error)
    }*/

}

function popElement()
{

    
    const tx = db.transaction("booking_table","readwrite")
    const ptab = tx.objectStore("booking_table")
    const request = ptab.openCursor()
    request.onsuccess = e => {
        const cursor = e.target.result
        if (cursor) {
            var name=cursor.key;
            var age=cursor.value.age;
            
            ptab.delete(name);
            alert('deleted!!')

            //do something with the cursor
            
        }
    }

}



window.addEventListener('online',  updateIndicator);
window.addEventListener('offline',  updateIndicator);
var btnView=document.getElementById('sub');
btnView.addEventListener('click',submitPress);

var btntrans=document.getElementById('transfer');
btntrans.addEventListener('click',transferElement);