{
"log": {
"loglevel": "warning",
"access": "./access.log"
},

"api": {
"services": [
"HandlerService",
"LoggerService",
"StatsService"
],
"tag": "api"
},
"inbounds": [
{
"listen": "127.0.0.1",
"port": 62789,
"protocol": "dokodemo-door",
"settings": {
"address": "127.0.0.1"
},
"tag": "api"
}
],
"outbounds": [
{
"protocol": "vless",
"settings": {
"vnext": [
{
"address": "d1svuiyng5h8mc.cloudfront.net",
"port": 443,
"users": [
{
"id": "1BB98B8F-1118-1636-672C-6BB9BCF3D4E0",
"encryption": "none"
}
]
}
],
"decryption": "none"
},
"streamSettings": {
"network": "ws",
"security": "tls",
"tlsSettings": {
"serverName": "d1svuiyng5h8mc.cloudfront.net",
"allowInsecure": false,
"alpn": ["http/1.1"]
},
"wsSettings": {
"path": "/",
"host": "d1svuiyng5h8mc.cloudfront.net"
}
},
"sniffing": {
"enabled": true,
"destOverride": ["http", "tls"]
}
}
],
"policy": {
"levels": {
"0": {
"statsUserUplink": true,
"statsUserDownlink": true
}
},
"system": {
"statsInboundDownlink": true,
"statsInboundUplink": true
}
},
"routing": {
"rules": [
{
"inboundTag": [
"api"
],
"outboundTag": "api",
"type": "field"
},
{
"ip": [
"geoip:private"
],
"outboundTag": "blocked",
"type": "field"
},
{
"outboundTag": "blocked",
"protocol": [
"bittorrent"
],
"type": "field"
}
]
},
"stats": {}
}
