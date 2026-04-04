# Schedule Generator for RoboCup

Currently the code only generates a schedule for the round robin phase. In the small division we currently have 21 qualified teams. That means:  
- 11 hours per day divided into 15min slots means 44 time slots per day
- Round Robin would be 210 games meaning we would need 5 days

## Example Schedule for the Small division:
```txt
Day 1 | 09:00 | Field 2 | Blenders FC vs Bold Hearts
Day 1 | 09:15 | Field 3 | RO:BIT vs Berlin United
Day 1 | 09:30 | Field 1 | WF Wolves vs ZJUDancer
Day 1 | 09:45 | Field 2 | ITAndroids vs Bold Hearts
Day 1 | 10:00 | Field 3 | Invic vs CAU Mountain&Sea
Day 1 | 10:15 | Field 1 | KHUBER vs Blenders FC
Day 1 | 10:30 | Field 2 | Mountain vs Berlin United
Day 1 | 10:45 | Field 3 | RO:BIT vs ZJUDancer
Day 1 | 11:00 | Field 1 | SABANA HERONS vs WF Wolves
Day 1 | 11:15 | Field 2 | Barelang FC vs GeoHBots
Day 1 | 11:30 | Field 4 | Hamburg Bit-Bots vs EWS Bascorro
Day 1 | 11:45 | Field 3 | HUST-HRT vs Colmillos ITAM
Day 1 | 12:00 | Field 1 | I-Kid vs CAU Mountain&Sea
Day 1 | 12:15 | Field 4 | ICHIRO ITS vs Bold Hearts
Day 1 | 12:30 | Field 3 | Invic vs Blenders FC
Day 1 | 12:45 | Field 1 | ITAndroids vs Berlin United
Day 1 | 13:00 | Field 2 | Mountain vs ZJUDancer
Day 1 | 13:15 | Field 4 | NUbots vs WF Wolves
Day 1 | 13:30 | Field 1 | RO:BIT vs SABANA HERONS
Day 1 | 13:45 | Field 2 | Barelang FC vs EWS Bascorro
Day 1 | 14:00 | Field 4 | GeoHBots vs Colmillos ITAM
Day 1 | 14:15 | Field 1 | Hamburg Bit-Bots vs CAU Mountain&Sea
Day 1 | 14:30 | Field 2 | HUST-HRT vs Bold Hearts
Day 1 | 14:45 | Field 4 | I-Kid vs Blenders FC
Day 1 | 15:00 | Field 1 | ICHIRO ITS vs Berlin United
Day 1 | 15:15 | Field 2 | ITAndroids vs ZJUDancer
Day 1 | 15:30 | Field 3 | KHUBER vs WF Wolves
Day 1 | 15:45 | Field 4 | Mountain vs SABANA HERONS
Day 1 | 16:00 | Field 2 | NUbots vs RO:BIT
Day 1 | 16:15 | Field 1 | Barelang FC vs Colmillos ITAM
Day 1 | 16:30 | Field 4 | EWS Bascorro vs CAU Mountain&Sea
Day 1 | 16:45 | Field 2 | GeoHBots vs Bold Hearts
Day 1 | 17:00 | Field 1 | Hamburg Bit-Bots vs Blenders FC
Day 1 | 17:15 | Field 3 | HUST-HRT vs Berlin United
Day 1 | 17:30 | Field 2 | ICHIRO ITS vs ZJUDancer
Day 1 | 17:45 | Field 1 | Invic vs WF Wolves
Day 1 | 18:00 | Field 3 | ITAndroids vs SABANA HERONS
Day 1 | 18:15 | Field 2 | KHUBER vs RO:BIT
Day 1 | 18:30 | Field 1 | Mountain vs NUbots
Day 1 | 18:45 | Field 3 | Barelang FC vs CAU Mountain&Sea
Day 1 | 19:00 | Field 2 | Colmillos ITAM vs Bold Hearts
Day 1 | 19:15 | Field 1 | EWS Bascorro vs Blenders FC
Day 1 | 19:30 | Field 3 | GeoHBots vs Berlin United
Day 1 | 19:45 | Field 2 | HUST-HRT vs ZJUDancer
Day 2 | 09:00 | Field 1 | I-Kid vs WF Wolves
Day 2 | 09:15 | Field 3 | ICHIRO ITS vs SABANA HERONS
Day 2 | 09:30 | Field 2 | Invic vs RO:BIT
Day 2 | 09:45 | Field 1 | ITAndroids vs NUbots
Day 2 | 10:00 | Field 3 | KHUBER vs Mountain
Day 2 | 10:15 | Field 2 | Barelang FC vs Bold Hearts
Day 2 | 10:30 | Field 1 | CAU Mountain&Sea vs Blenders FC
Day 2 | 10:45 | Field 3 | Colmillos ITAM vs Berlin United
Day 2 | 11:00 | Field 2 | GeoHBots vs ZJUDancer
Day 2 | 11:15 | Field 1 | Hamburg Bit-Bots vs WF Wolves
Day 2 | 11:30 | Field 3 | HUST-HRT vs SABANA HERONS
Day 2 | 11:45 | Field 2 | I-Kid vs RO:BIT
Day 2 | 12:00 | Field 1 | ICHIRO ITS vs NUbots
Day 2 | 12:15 | Field 3 | Invic vs Mountain
Day 2 | 12:30 | Field 2 | ITAndroids vs KHUBER
Day 2 | 12:45 | Field 1 | Barelang FC vs Blenders FC
Day 2 | 13:00 | Field 3 | Bold Hearts vs Berlin United
Day 2 | 13:15 | Field 2 | Colmillos ITAM vs ZJUDancer
Day 2 | 13:30 | Field 1 | EWS Bascorro vs WF Wolves
Day 2 | 13:45 | Field 3 | GeoHBots vs SABANA HERONS
Day 2 | 14:00 | Field 2 | Hamburg Bit-Bots vs RO:BIT
Day 2 | 14:15 | Field 1 | HUST-HRT vs NUbots
Day 2 | 14:30 | Field 3 | I-Kid vs Mountain
Day 2 | 14:45 | Field 2 | ICHIRO ITS vs KHUBER
Day 2 | 15:00 | Field 1 | Invic vs ITAndroids
Day 2 | 15:15 | Field 3 | Barelang FC vs Berlin United
Day 2 | 15:30 | Field 2 | CAU Mountain&Sea vs WF Wolves
Day 2 | 15:45 | Field 1 | Colmillos ITAM vs SABANA HERONS
Day 2 | 16:00 | Field 3 | EWS Bascorro vs RO:BIT
Day 2 | 16:15 | Field 2 | GeoHBots vs NUbots
Day 2 | 16:30 | Field 1 | Hamburg Bit-Bots vs Mountain
Day 2 | 16:45 | Field 3 | HUST-HRT vs KHUBER
Day 2 | 17:00 | Field 2 | I-Kid vs ITAndroids
Day 2 | 17:15 | Field 1 | ICHIRO ITS vs Invic
Day 2 | 17:30 | Field 3 | Bold Hearts vs ZJUDancer
Day 2 | 17:45 | Field 2 | I-Kid vs EWS Bascorro
Day 2 | 18:00 | Field 1 | ICHIRO ITS vs Colmillos ITAM
Day 2 | 18:15 | Field 3 | HUST-HRT vs GeoHBots
Day 2 | 18:30 | Field 2 | Barelang FC vs Hamburg Bit-Bots
Day 2 | 18:45 | Field 1 | NUbots vs Blenders FC
Day 2 | 19:00 | Field 3 | Mountain vs Bold Hearts
Day 2 | 19:15 | Field 2 | KHUBER vs CAU Mountain&Sea
Day 2 | 19:30 | Field 1 | ITAndroids vs Colmillos ITAM
Day 2 | 19:45 | Field 3 | Invic vs EWS Bascorro
Day 3 | 09:00 | Field 2 | ICHIRO ITS vs GeoHBots
Day 3 | 09:15 | Field 1 | I-Kid vs Hamburg Bit-Bots
Day 3 | 09:30 | Field 3 | Barelang FC vs HUST-HRT
Day 3 | 09:45 | Field 2 | WF Wolves vs Berlin United
Day 3 | 10:00 | Field 1 | SABANA HERONS vs Blenders FC
Day 3 | 10:15 | Field 3 | RO:BIT vs Bold Hearts
Day 3 | 10:30 | Field 2 | NUbots vs CAU Mountain&Sea
Day 3 | 10:45 | Field 1 | Mountain vs Colmillos ITAM
Day 3 | 11:00 | Field 3 | KHUBER vs EWS Bascorro
Day 3 | 11:15 | Field 2 | ITAndroids vs GeoHBots
Day 3 | 11:30 | Field 1 | Invic vs Hamburg Bit-Bots
Day 3 | 11:45 | Field 3 | ICHIRO ITS vs HUST-HRT
Day 3 | 12:00 | Field 2 | Barelang FC vs I-Kid
Day 3 | 12:15 | Field 1 | ZJUDancer vs Blenders FC
Day 3 | 12:30 | Field 3 | WF Wolves vs Bold Hearts
Day 3 | 12:45 | Field 2 | SABANA HERONS vs CAU Mountain&Sea
Day 3 | 13:00 | Field 1 | RO:BIT vs Colmillos ITAM
Day 3 | 13:15 | Field 3 | NUbots vs EWS Bascorro
Day 3 | 13:30 | Field 2 | Mountain vs GeoHBots
Day 3 | 13:45 | Field 1 | KHUBER vs Hamburg Bit-Bots
Day 3 | 14:00 | Field 3 | ITAndroids vs HUST-HRT
Day 3 | 14:15 | Field 2 | Invic vs I-Kid
Day 3 | 14:30 | Field 1 | Barelang FC vs ICHIRO ITS
Day 3 | 14:45 | Field 3 | Berlin United vs Blenders FC
Day 3 | 15:00 | Field 2 | ZJUDancer vs CAU Mountain&Sea
Day 3 | 15:15 | Field 1 | WF Wolves vs Colmillos ITAM
Day 3 | 15:30 | Field 3 | SABANA HERONS vs EWS Bascorro
Day 3 | 15:45 | Field 2 | RO:BIT vs GeoHBots
Day 3 | 16:00 | Field 1 | NUbots vs Hamburg Bit-Bots
Day 3 | 16:15 | Field 3 | Mountain vs HUST-HRT
Day 3 | 16:30 | Field 2 | KHUBER vs I-Kid
Day 3 | 16:45 | Field 1 | ITAndroids vs ICHIRO ITS
Day 3 | 17:00 | Field 3 | Barelang FC vs Invic
Day 3 | 17:15 | Field 2 | Berlin United vs CAU Mountain&Sea
Day 3 | 17:30 | Field 1 | ZJUDancer vs EWS Bascorro
Day 3 | 17:45 | Field 3 | WF Wolves vs GeoHBots
Day 3 | 18:00 | Field 2 | SABANA HERONS vs Hamburg Bit-Bots
Day 3 | 18:15 | Field 1 | RO:BIT vs HUST-HRT
Day 3 | 18:30 | Field 3 | NUbots vs I-Kid
Day 3 | 18:45 | Field 2 | Mountain vs ICHIRO ITS
Day 3 | 19:00 | Field 1 | KHUBER vs Invic
Day 3 | 19:15 | Field 3 | Barelang FC vs ITAndroids
Day 3 | 19:30 | Field 2 | Bold Hearts vs CAU Mountain&Sea
Day 3 | 19:45 | Field 1 | Blenders FC vs Colmillos ITAM
Day 4 | 09:00 | Field 3 | Berlin United vs EWS Bascorro
Day 4 | 09:15 | Field 4 | ZJUDancer vs Hamburg Bit-Bots
Day 4 | 09:30 | Field 2 | WF Wolves vs HUST-HRT
Day 4 | 09:45 | Field 3 | SABANA HERONS vs I-Kid
Day 4 | 10:00 | Field 1 | RO:BIT vs ICHIRO ITS
Day 4 | 10:15 | Field 2 | NUbots vs Invic
Day 4 | 10:30 | Field 3 | Mountain vs ITAndroids
Day 4 | 10:45 | Field 1 | Barelang FC vs KHUBER
Day 4 | 11:00 | Field 2 | CAU Mountain&Sea vs Colmillos ITAM
Day 4 | 11:15 | Field 3 | Bold Hearts vs EWS Bascorro
Day 4 | 11:30 | Field 1 | Blenders FC vs GeoHBots
Day 4 | 11:45 | Field 2 | Berlin United vs Hamburg Bit-Bots
Day 4 | 12:00 | Field 3 | ZJUDancer vs I-Kid
Day 4 | 12:15 | Field 1 | WF Wolves vs ICHIRO ITS
Day 4 | 12:30 | Field 2 | SABANA HERONS vs Invic
Day 4 | 12:45 | Field 3 | RO:BIT vs ITAndroids
Day 4 | 13:00 | Field 1 | NUbots vs KHUBER
Day 4 | 13:15 | Field 2 | Barelang FC vs Mountain
Day 4 | 13:30 | Field 3 | Colmillos ITAM vs EWS Bascorro
Day 4 | 13:45 | Field 1 | CAU Mountain&Sea vs GeoHBots
Day 4 | 14:00 | Field 2 | Bold Hearts vs Hamburg Bit-Bots
Day 4 | 14:15 | Field 3 | Blenders FC vs HUST-HRT
Day 4 | 14:30 | Field 1 | Berlin United vs I-Kid
Day 4 | 14:45 | Field 2 | ZJUDancer vs Invic
Day 4 | 15:00 | Field 3 | WF Wolves vs ITAndroids
Day 4 | 15:15 | Field 1 | SABANA HERONS vs KHUBER
Day 4 | 15:30 | Field 2 | RO:BIT vs Mountain
Day 4 | 15:45 | Field 3 | Barelang FC vs NUbots
Day 4 | 16:00 | Field 1 | EWS Bascorro vs GeoHBots
Day 4 | 16:15 | Field 2 | Colmillos ITAM vs Hamburg Bit-Bots
Day 4 | 16:30 | Field 3 | CAU Mountain&Sea vs HUST-HRT
Day 4 | 16:45 | Field 1 | Bold Hearts vs I-Kid
Day 4 | 17:00 | Field 2 | Blenders FC vs ICHIRO ITS
Day 4 | 17:15 | Field 3 | Berlin United vs Invic
Day 4 | 17:30 | Field 1 | ZJUDancer vs KHUBER
Day 4 | 17:45 | Field 2 | WF Wolves vs Mountain
Day 4 | 18:00 | Field 3 | SABANA HERONS vs NUbots
Day 4 | 18:15 | Field 1 | Barelang FC vs RO:BIT
Day 4 | 18:30 | Field 2 | GeoHBots vs Hamburg Bit-Bots
Day 4 | 18:45 | Field 3 | EWS Bascorro vs HUST-HRT
Day 4 | 19:00 | Field 1 | Colmillos ITAM vs I-Kid
Day 4 | 19:15 | Field 2 | CAU Mountain&Sea vs ICHIRO ITS
Day 4 | 19:30 | Field 4 | Bold Hearts vs Invic
Day 4 | 19:45 | Field 1 | Blenders FC vs ITAndroids
Day 5 | 09:00 | Field 3 | Berlin United vs KHUBER
Day 5 | 09:15 | Field 2 | ZJUDancer vs NUbots
Day 5 | 09:30 | Field 1 | WF Wolves vs RO:BIT
Day 5 | 09:45 | Field 3 | Barelang FC vs SABANA HERONS
Day 5 | 10:00 | Field 2 | Hamburg Bit-Bots vs HUST-HRT
Day 5 | 10:15 | Field 1 | GeoHBots vs I-Kid
Day 5 | 10:30 | Field 3 | EWS Bascorro vs ICHIRO ITS
Day 5 | 10:45 | Field 2 | Colmillos ITAM vs Invic
Day 5 | 11:00 | Field 1 | CAU Mountain&Sea vs ITAndroids
Day 5 | 11:15 | Field 4 | Bold Hearts vs KHUBER
Day 5 | 11:30 | Field 3 | Blenders FC vs Mountain
Day 5 | 11:45 | Field 1 | Berlin United vs NUbots
Day 5 | 12:00 | Field 2 | ZJUDancer vs SABANA HERONS
Day 5 | 12:15 | Field 3 | Barelang FC vs WF Wolves
Day 5 | 12:30 | Field 1 | HUST-HRT vs I-Kid
Day 5 | 12:45 | Field 2 | Hamburg Bit-Bots vs ICHIRO ITS
Day 5 | 13:00 | Field 3 | GeoHBots vs Invic
Day 5 | 13:15 | Field 1 | EWS Bascorro vs ITAndroids
Day 5 | 13:30 | Field 2 | Colmillos ITAM vs KHUBER
Day 5 | 13:45 | Field 4 | CAU Mountain&Sea vs Mountain
Day 5 | 14:00 | Field 3 | Bold Hearts vs NUbots
Day 5 | 14:15 | Field 2 | Blenders FC vs RO:BIT
Day 5 | 14:30 | Field 4 | Berlin United vs SABANA HERONS
Day 5 | 14:45 | Field 3 | Barelang FC vs ZJUDancer
Day 5 | 15:00 | Field 1 | I-Kid vs ICHIRO ITS
Day 5 | 15:15 | Field 4 | HUST-HRT vs Invic
Day 5 | 15:30 | Field 2 | Hamburg Bit-Bots vs ITAndroids
Day 5 | 15:45 | Field 1 | GeoHBots vs KHUBER
Day 5 | 16:00 | Field 3 | EWS Bascorro vs Mountain
Day 5 | 16:15 | Field 4 | Colmillos ITAM vs NUbots
Day 5 | 16:30 | Field 1 | CAU Mountain&Sea vs RO:BIT
Day 5 | 16:45 | Field 3 | Bold Hearts vs SABANA HERONS
Day 5 | 17:00 | Field 2 | Blenders FC vs WF Wolves
Day 5 | 17:15 | Field 1 | Berlin United vs ZJUDancer
```