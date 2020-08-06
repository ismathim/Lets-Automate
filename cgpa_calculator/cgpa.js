function formatCGPA(value){
				value =value*100/100;
        value=value.toFixed(2);
        return "CGPA... "+value;
			}
      function update(){
					let subject=Number(document.getElementById("splitInput").value);

					let bill_1= Number(document.getElementById("yourBill_1").value);
					let grade_1= document.getElementById("tipInput_1").value;
					let total_1=bill_1*grade_1;

					let bill_2= Number(document.getElementById("yourBill_2").value);
					let grade_2= document.getElementById("tipInput_2").value;
					let total_2=bill_2*grade_2;

					let bill_3= Number(document.getElementById("yourBill_3").value);
					let grade_3= document.getElementById("tipInput_3").value;
					let total_3=bill_1*grade_3;

					let bill_4= Number(document.getElementById("yourBill_4").value);
					let grade_4= document.getElementById("tipInput_4").value;
					let total_4=bill_1*grade_4;

					let bill_5= Number(document.getElementById("yourBill_5").value);
					let grade_5= document.getElementById("tipInput_5").value;
					let total_5=bill_5*grade_5;

					let bill_6= Number(document.getElementById("yourBill_6").value);
					let grade_6= document.getElementById("tipInput_6").value;
					let total_6=bill_6*grade_6;

					let bill_7= Number(document.getElementById("yourBill_7").value);
					let grade_7= document.getElementById("tipInput_7").value;
					let total_7=bill_7*grade_7;

					let bill_8= Number(document.getElementById("yourBill_8").value);
					let grade_8= document.getElementById("tipInput_8").value;
					let total_8=bill_8*grade_8;
					let total_bill=(bill_1+bill_2+bill_3+bill_4+bill_5+bill_6+bill_7+bill_8);
					let total=((bill_1*grade_1)+(bill_2*grade_2)+(bill_3*grade_3)+(bill_4*grade_4)+(bill_5*grade_5)+(bill_6*grade_6)+(bill_7*grade_7)+(bill_8*grade_8))/(total_bill);


					document.getElementById("totalWithTip_1").innerHTML=total_1;
					document.getElementById("tipPercent_1").innerHTML=grade_1+" Point";

					document.getElementById("totalWithTip_2").innerHTML=total_2;
					document.getElementById("tipPercent_2").innerHTML=grade_2+" Point";

					document.getElementById("totalWithTip_3").innerHTML=total_3;
					document.getElementById("tipPercent_3").innerHTML=grade_3+" Point";

					document.getElementById("totalWithTip_4").innerHTML=total_4;
					document.getElementById("tipPercent_4").innerHTML=grade_4+" Point";

					document.getElementById("totalWithTip_5").innerHTML=total_5;
					document.getElementById("tipPercent_5").innerHTML=grade_5+" Point";

					document.getElementById("totalWithTip_6").innerHTML=total_6;
					document.getElementById("tipPercent_6").innerHTML=grade_6+" Point";

					document.getElementById("totalWithTip_7").innerHTML=total_7;
					document.getElementById("tipPercent_7").innerHTML=grade_7+" Point";

					document.getElementById("totalWithTip_8").innerHTML=total_8;
					document.getElementById("tipPercent_8").innerHTML=grade_8+" Point";

					document.getElementById("splitValue").innerHTML=subject;
					document.getElementById("totalWithTip").innerHTML=formatCGPA(total);
				  console.log(bill_1, grade_1);
				}


      let container= document.getElementById("container");
      container.addEventListener("input",update);
