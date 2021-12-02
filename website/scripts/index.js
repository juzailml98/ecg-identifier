
window.onload=( hello())

function hello(){
   files = document.getElementsByClassName('submit-form')[0];
  submit = document.getElementById('submitFiles');
   warning = document.getElementById('warning');
   results=document.getElementsByClassName("results")[0];


}
files.addEventListener("click",function(){
  results.innerText="you have uploaded the file successfully.dont refresh till the result come";
  results.style.display="block";

})
