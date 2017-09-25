import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='GuestQueue')

channel.basic_publish(exchange='GuestExchange',
                      routing_key='GuestExchange-GuestQueue',
                      body='{"type":"webhook_event","id":"8365e511-753a-40d0-92b2-0209fefb586b","created_at":"2017-08-21T06:42:47-07:00","trigger":"FILE.UPLOADED","webhook":{"id":"6195144","type":"webhook"},"created_by":{"type":"user","id":"226542005","name":"Jason Pully","login":"jwpully@wm.edu"},"source":{"id":"212477128297","type":"file","file_version":{"type":"file_version","id":"225419869417","sha1":"865b42442d241373849fe7384871feef56e8d426"},"sequence_id":"1","etag":"1","sha1":"865b42442d241373849fe7384871feef56e8d426","name":"data.xlsx","description":"","size":8919,"path_collection":{"total_count":5,"entries":[{"type":"folder","id":"0","sequence_id":null,"etag":null,"name":"All Files"},{"type":"folder","id":"17045061440","sequence_id":"1","etag":"1","name":"EISProcess"},{"type":"folder","id":"17073942349","sequence_id":"0","etag":"0","name":"devl"},{"type":"folder","id":"31999358107","sequence_id":"0","etag":"0","name":"Axiom"},{"type":"folder","id":"34006120206","sequence_id":"0","etag":"0","name":"OMBA"}]},"created_at":"2017-08-18T13:50:47-07:00","modified_at":"2017-08-21T06:42:47-07:00","trashed_at":null,"purged_at":null,"content_created_at":"2017-08-18T12:13:26-07:00","content_modified_at":"2017-08-18T12:13:26-07:00","created_by":{"type":"user","id":"226542005","name":"Jason Pully","login":"jwpully@wm.edu"},"modified_by":{"type":"user","id":"226542005","name":"Jason Pully","login":"jwpully@wm.edu"},"owned_by":{"type":"user","id":"842950848","name":"EIS Process","login":"AppUser_319765_SPzhjAH6sq@boxdevedition.com"},"shared_link":null,"parent":{"type":"folder","id":"34006120206","sequence_id":"0","etag":"0","name":"OMBA"},"item_status":"active"},"additional_info":[]}')
print(" [x] Sent 'Hello World!'")

connection.close()