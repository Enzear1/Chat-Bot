const express = require('express');
const app = express();
const router = express.Router();

chatUSERS = []
total = 0
chatDATA = {'total' : 0}

router.get('/usersEvent',function(req,res) {
    console.log(req.query)
    if(req.query['eventName'] == 'addUserName') {
        if(chatUSERS.includes(req.query['name'])) {
            res.send('201')
        } else {
            chatUSERS.push(req.query['name'])
            res.send('301')
        }
    } else if(req.query['eventName'] == 'sendMessage') {
        total += 1
        chatDATA['total'] = total
        chatDATA[String(total)] = {
            [req.query['name']] : req.query['msg']
        }
        console.log(chatUSERS)
        console.log(chatDATA)
        res.send('301')
    }
    console.log(chatUSERS)
    console.log(chatDATA)
})
router.get('/getChat',function(req,res) {
    res.send(chatDATA)
})

app.use('/', router);
app.listen(process.env.port || 3000);

console.log('Running at Port 3000');
