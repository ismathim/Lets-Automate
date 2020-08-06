
      function formatMoney(value){
        value =Math.ceil(value*100)/100;
        value=value.toFixed(2);
        return "$ "+value;
      }

      function formatPerson(value){
        if (value==="1") return value+" Person";
        return value+" People";
      }

      function update(){
      let bill=  Number(document.getElementById('yourBill').value);
      let tipPercent=  document.getElementById('tipInput').value;
      let split=  document.getElementById('splitInput').value;

      let tipValue= bill*(tipPercent/100);
      let tipEach=tipValue/split;

      let newBillEach= (bill+tipValue)/split;

      document.getElementById("tipPercent").innerHTML=tipPercent+"%";
      document.getElementById("tipValue").innerHTML=formatMoney(tipValue);
      document.getElementById("totalWithTip").innerHTML=formatMoney(bill+tipValue);
      document.getElementById("splitValue").innerHTML=formatPerson(split);
      document.getElementById("billEach").innerHTML=formatMoney(newBillEach);
      document.getElementById("tipEach").innerHTML=formatMoney(tipEach);
      console.log(tipValue);

      }
      let container= document.getElementById("container");
      container.addEventListener("input",update);
