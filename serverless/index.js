/*
exports.handler = async (event) => {
    // TODO implement
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    };
    return response;
};
*/

'use strict';

console.log("Loading function");

let AWS = require("aws-sdk");
let docClient = new AWS.DynamoDB.DocumentClient();
let params;
let tableName;

exports.get = async (event, context) => {
    console.debug("get event:", event);

    if (tableName == null) {
        tableName = process.env.TABLE_NAME;
    }
    params = {
        TableName: tableName,
        Key: {
            "user_id": "*",
            "timestamp": "*"
        }
    };
    console.debug(params.Key);

    return await new Promise((resolve, reject) => {
        //docClient.get(params, (error, data) => {
        docClient.scan(params, (error, data) => {
            if (error) {
                console.error(`get ERROR=${error.stack}`);
                resolve({
                    statusCode: 400,
                    error: `Could not get data: ${error.stack}`
                });
            } else {
                console.debug(`get data=${JSON.stringify(data)}`);
                resolve({
                    statusCode: 200,
                    body: JSON.stringify(data)
                });
            }
        });
    });
};

exports.post = async (event, context) => {
    console.debug("postMessage event:", event);

    if (tableName == null) {
        tableName = process.env.TABLE_NAME;
    }
    console.debug("post event.body:", event.body);

    let parsedBody = JSON.parse(JSON.stringify(event.body));

    params = {
        TableName: tableName,
        Item: parsedBody.Item
    };
    console.debug(params);

    return await new Promise((resolve, reject) => {
        docClient.put(params, (error, data) => {
            if (error) {
                console.error(`post ERROR=${error.stack}`);
                resolve({
                    statusCode: 400,
                    error: `Could not post data: ${error.stack}`
                });
            } else {
                console.info(`post data=${JSON.stringify(data)}`);
                resolve({
                    statusCode: 201,
                    body: JSON.stringify(data)
                });
            }
        });
    });
};

exports.put = async (event, context) => {
    console.debug("put event:", event);

    if (tableName == null) {
        tableName = process.env.TABLE_NAME;
    }

    let parsedBody = JSON.parse(event.body);

    params = {
        TableName: tableName,
        Key: {
            "date": event.pathParameters.date,
            "time": event.queryStringParameters.time
        },
        UpdateExpression: parsedBody.UpdateExpression,
        ExpressionAttributeValues: parsedBody.ExpressionAttributeValues

    };
    console.debug(params);

    return await new Promise((resolve, reject) => {
        docClient.update(params, (error, data) => {
            if (error) {
                console.error(`put ERROR=${error.stack}`);
                resolve({
                    statusCode: 400,
                    error: `Could not update data: ${error.stack}`
                });
            } else {
                console.info(`put data=${JSON.stringify(data)}`);
                resolve({
                    statusCode: 204,
                    body: JSON.stringify(data)
                });
            }
        });
    });
};

exports.delete = async (event, context) => {
    console.debug("delete event:", event);

    if (tableName == null) {
        tableName = process.env.TABLE_NAME;
    }
    params = {
        TableName: tableName,
        Key: {
            "date": event.pathParameters.date,
            "time": event.queryStringParameters.time
        }
    };
    console.debug(params.Key);

    return await new Promise((resolve, reject) => {
        docClient.delete(params, (error, data) => {
            if (error) {
                console.error(`delete ERROR=${error.stack}`);
                resolve({
                    statusCode: 400,
                    error: `Could not delete data: ${error.stack}`
                });
            } else {
                console.info(`delete data=${JSON.stringify(data)}`);
                resolve({
                    statusCode: 200,
                    body: JSON.stringify(data)
                });
            }
        });
    });
};