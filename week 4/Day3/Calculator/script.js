var resultValue = "";

function number(num) {
  resultValue += num;
  document.getElementById("result").value = resultValue;
}

function operator(op) {
  resultValue += op;
  document.getElementById("result").value = resultValue;
}

function equal() {
  var result = eval(resultValue);
  document.getElementById("result").value = result;
  resultValue = result.toString();
}

function reset() {
  resultValue = "";
  document.getElementById("result").value = "";
}

function clear() {
  resultValue = resultValue.slice(0, -1);
  document.getElementById("result").value = resultValue;
}