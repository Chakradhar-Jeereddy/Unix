# Nginx
1. http/web server
2. reverse proxy
3. load balancer

proxy: On behalf of someone

## Forword proxy
On behalf of client

Mobile -> VPN(US) -> facebook.com and get the response to VPN --> Mobile
hiding client identity, access restriction and trafic filtering.

## Reverse proxy
On behalf of server

Hides the backend servers(security)
Load balancing
SSL termination
Caching (Faster access for subsequent users)

```
vi /etc/nginx/nginx.conf

http {
  upstream frontend {
    server frontend-1.chakra86.shop;
    server frontend-2.chakra86.shop;
  }


location / {
          proxy_pass  http://frontend;
        }
```

- http://slb.chakra86.shop/api/transaction

## Troubleshooting
 - Right lick and click **Inspect** > **Network**
HTTP methods and status codes
GET
POST: converts into {amount: "100", desc: "snacks"} and posts.

Response codes
2xx -> Success
3XX -> Redirection/cache  304 - not modified (gets it from cache, not going to database)
4xx -> Client side errors (400: bad request, 401: authorization error, 403: Forbidden. No access to you. 404: Not found (what you're serching not there in server)
http://slb.chakra86.shop/efsfs -> 404

5xx - server side errors 
500 - Problem inside servers
502 - bad gateway
503 - Service unavailable

## check logs
- Loadbalancer - /var/log/nginx/access.log or error.log (HTTP errors)
- backend - /var/log/messages (curd operations)
- /usr/share/nginx/html (web pages)
- /etc/nginx/nginx.conf (Config file)

systemctl ...
netstat -nltp
telnet ip port
ps -ef
inspect and check on browser

curl http://localhost:8080/health



- 
504 - Gateway timeout, backend servers are down






