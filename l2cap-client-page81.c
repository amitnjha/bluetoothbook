#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <bluetooth/bluetooth.h>
#include <bluetooth/l2cap.h>


int main(int argc, char* argv[]){
  struct sockaddr_l2 addr = {0};
  int s, status ;
  char dest[18] = "<>";
  
  if(argc < 2){
    fprintf(stderr, "usage:%s <btaddr>\n", argv[0]);
    return 1;
  }

  strncpy(dest, argv[1], 18);
  
  //allocate a socket
  s = socket(AF_BLUETOOTH, SOCK_SEQPACKET, BTPROTO_L2CAP);
  //set the connection param who to connect to.
  
  addr.l2_family = AF_BLUETOOTH;
  addr.l2_psm = htobs(0x1001);
  
  //connect to server
  status = connect(s, (struct sockaddr*)&addr, sizeof(addr));
  
  //send a message
  if(0 == status){
    status = send (s, "hello!", 6, 0 );
  }
  
  if (status < 0)
    perror("Error");
  close(s);
  return 0;
}
