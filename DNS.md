## DNS workflow
- When we query DNS it returns the IP of the site we are trying to access.
- Example - search for facebook.com
- **Browser** > **Borwser Cache** > **OS** > **OS cache** > **ISP DNS Resolver** > **ISP DNS Cache** > **root server** > **TLD** > **Domain Authority** > **hostinger**

- root server will tell which TLD is going to return the IP. 13 companies are managing root servers.

- ISP DNS resolver: A software running in ISP server to fetch IP address of the domain.
- ICNN - Internet cooperation assigned names and numbers.
- TLD: Top level domain (.uk,.us..com,.ai,.in,.org,.elu)
- Domain authority: Why can my the domain from these authority.
- When we buy domain, it will first check if requested domain is available. If yes, it will take the personal details and ask TLD to block the domain and TLD will pay
- commission to DA.
- Once the domain is purchased, a name servers are assign to domain. These name servers resolve the DNS. We can shift domain authority to AWS by providing the AWS name
- servers to hostinger and removing hostinger name servers.

- In AWS route53 service create hosted zone, provide the purchased domain name, it will generate name servers for this domain, update that in hostinger website
ns-825.awsdns-39.net
ns-1434.awsdns-51.org
ns-1739.awsdns-25.co.uk
ns-35.awsdns-04.com


Create records
## Record types
 1. A: IPV4 address
 2. CNAME: Another domain
 3. MX: Mail server
 4. TxT: Domain verification purpose
 5. AAAA: IPv6 Address
 6. SOA: Who is controling name servers? AWS
 7. NS: Name servers

- Create record type A for mysql, backend and frontend
- mysql.chakra86.shop - private IP and test record
- backend.chakra86.shop - private IP and test record
- frontend.chakra86.shop - publick IP and test record

 nslookup the three recods and it should resolve the name and retrun IP address.
 

- TTL (time to live): Decrease or increase DNS overhead.
- Duration of the record or IP in cache. After the TTL it will again query the DNS.
- Put higher value for static website.
- Put lower value for migrations, where the IP changes.

