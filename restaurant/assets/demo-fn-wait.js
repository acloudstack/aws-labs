function sleep(delay) {
    var start = new Date().getTime();
    while (new Date().getTime() < start + delay);
}

exports.handler = function(event, context) {
  console.debug(event);
  console.debug('Start - Sleep for 200 miliseconds');
  sleep(2000);
  console.debug('End - Sleep for 200 miliseconds');
  
  var retVal= { 
    "message": 'Hello from Lambda!',
    "error-info" : {
      "Error": "Error",
      "Cause": "Test Error"
    }
  };
  
  const response = {
      statusCode: 200,
      body: JSON.stringify(retVal)
  };
  console.debug(retVal)
  return retVal;
}