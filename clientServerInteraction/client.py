#!/usr/bin/python
import xmlrpclib
import sys

proxy = xmlrpclib.ServerProxy("http://localhost:8080/RPC2")
return_list = proxy.sample.addmultiply(float(sys.argv[1]),float(sys.argv[2]))
print return_list[0], " ", return_list[1]

# // /*
# //  * client.c
# //    Anush Rathod - 32914218
# //    Ritvik Verma - 32840122
# //  */

# // #include <stdio.h>
# // #include <stdlib.h>
# // #include "csapp.h"

# // int main(int argc, char **argv) 
# // {
# //     int clientfd;
# //     char *num1, *num2;
# //     char *host, *port;

# //     if (argc != 3) {
# //         fprintf(stderr, "usage: %s <num1> <num2>\n", argv[0]);
# //         exit(0);
# //     }

# //     num1 = argv[1];
# //     num2 = argv[2];

# //     host = "localhost";
# //     port = "8080";

# //     clientfd = Open_clientfd(host, port);

# //     rio_t rio; //robust I/O
# //     char buf[MAXLINE];
# //     char xml[MAXLINE];
# //     char *ptr;

# //     // send the arguments to server.py and read the output sent by server.py
# //     sprintf(xml,"<?xml version='1.0'?>\r\n""<methodCall>\r\n""<methodName>sample.addmultiply</methodName>\r\n""<params>\r\n""<param>\r\n""<value><double>%s</double></value>\r\n""</param>\r\n""<param>\r\n""<value><double>%s</double></value>\r\n""</param>\r\n""</params>\r\n""</methodCall>\n\n",num1,num2);

# //    //write the xml to the server
# //     sprintf(buf, "POST /RPC2 HTTP/1.1\r\n""Content-Type: text/xml\r\n""User-Agent: XML-RPC.NET\r\n""Content-Length: %d\r\n""Expect: 100-continue\r\n""Connection: Keep-Alive\r\n""Host: localhost:8080\r\n\n%s",strlen(xml),xml);

# //     Rio_writen(clientfd,buf,strlen(buf)); //write to server
 
# //     Rio_readinitb(&rio,clientfd); //read from server


# //     for (int i = 0; i < 13; i++){
# //         Rio_readlineb(&rio, buf, sizeof(buf)); //read from server

# //         if (i == 11 || i == 12)
# //         {
# //             ptr = strstr(buf,"double"); //find the location of <double>
# //             ptr = ptr + 7; //move the pointer to the first digit
# //             while(*ptr != '<') //while the digit is not <
# //             {

# //                 //round each answer to 1 decimal place
# //                 if (*ptr == '.')
# //                 {
# //                     ptr = ptr + 2;
# //                     if (*ptr >= '5' && *ptr != '<') //if the 2nd digit after '.' is >= 5
# //                     {
# //                         ptr--; //move the pointer to the first digit
# //                         *ptr = *ptr + 1; //add 1 to the first digit
# //                         ptr++; //move the pointer to the second digit
# //                         *ptr = '<'; //replace the second digit with <
# //                         ptr = ptr-2; //move the pointer to the '.'
# //                     }
# //                     else
# //                     {
# //                         *ptr = '<';
# //                         ptr= ptr-2;
# //                     }
# //                 }
# //                 printf("%c",(*ptr)); //print the digit
# //                 ptr++; //move the pointer to the next digit
                
# //             }
# //             printf("   "); //print a space
# //         }
# //     }


# //     printf("\r\n");
# //     Close(clientfd);
# //     exit(0);
# // }
