#include <stdio.h>
#include <string.h>
int main(int argc, char* argv[]) {
        if(argc == 2){
            printf("Validating license %s...\n", argv[1]);
            int len = strlen(argv[1]);
    //printf("Length of license is %d \n", len);
            int sum = 0;
            for(int i=0; i < len; i++){
                sum += argv[1][i];
            }
            if(sum == 532){
                    printf("Access Granted \n");
            }else{
                printf("Invalid license. \n");
            }
        }else{
                printf("Usage %s <liecense> \n", argv[0]);
                return 0;
        }
}
