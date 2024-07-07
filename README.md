# Hacking-tools
Program with tools for DDOS-attack

## How to use
```
$ python hack.py [ Type ] [ URL(for httpf) | IP(other than httpf) ] [ Port ]
```

### Type
- **httpf**( HTTP Flood ) : An attack that exhausts a web server's resources by sending a large number of HTTP requests.

- **hsl**( HTTP Slowloris ) : It ensures connectivity to the web server by sending HTTP headers at a very aggressive rate while maintaining server-relational connectivity.

- **rudy**( RUDY ) : An attack that exhausts server resources by sending POST requests very slowly.

- **synf**( SYN Flooding ) : An attack that exhausts server resources by sending a large number of TCP connection request packets (SYN packets).

- **udpf**( UDP Flooding ) : An attack that exhausts network bandwidth by sending large amounts of UDP packets to the target server.

- **help**( Help page ) : Help page. When using help, you do not need to enter IP and port.

### IP
IP of target. 
HTTP Flood does not accept this argument.

### URL 
URL of target. 
Except for HTTP Flood, all others do not accept this argument.

### Port
Port of target. 
HTTP Flood does not accept this argument.


