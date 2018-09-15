

window.onload = loadfromDB;

function loadfromDB(){
  $.ajax({
    type: "POST",
    url: "loadfromdb",
    data: {
           },
    success: callbackFunc
});
}

function newItem() {
    var itemI = document.getElementById("inputI").value;
    var ulI = document.getElementById("listI");
    var itemVal = document.getElementById("inputVal").value;
    var ulVal = document.getElementById("listVal");
    var li = document.createElement("li");
    li.appendChild(document.createTextNode("- " + itemI + ", " + itemVal));
    ulVal.appendChild(li);
    document.getElementById("inputI").value = "";
    document.getElementById("inputVal").value = "";
    li.onclick = removeItem;
    console.log("clicked");
   addtodb(itemI, itemVal);
   console.log("clicked2");

  }
  
  document.body.onkeyup = function(e) {
    if (e.keyCode == 13) {
      newItem();
    }
  };
  
  function removeItem(e) {
    console.log(e.target.parentElement.textContent);
    $.ajax({
      type: "POST",
      url: "removefromdb",
      data: { 'torem1' : e.target.parentElement.textContent.split(' ')[1].split(',')[0],
             },
      success: callbackFunc
  });
    e.target.parentElement.removeChild(e.target);
  }
  
  function addtodb(itemI, itemVal) {
    $.ajax({
      type: "POST",
      url: "addtodb",
      data: { item : itemI,
              val : itemVal,
             },
      success: callbackFunc
  });

  }

function callbackFunc(response) {
    // do something with the response
    console.log("We added to db");
}
