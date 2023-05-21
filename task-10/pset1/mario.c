#include <cs50.h>
#include <stdio.h>

int main()
{
    int rows;
    do
    {
        printf("Height: ");
        scanf("%d", &rows);
    }
    while (rows < 1 || rows > 8);

    for (int i = 1; i <= rows; i++)
    {

        for (int j = 1; j <= rows - i; j++)
        {
            printf(" ");
        }

        for (int j = 1; j <= i; j++)
        {
            printf("#");
        }

        printf("  ");

        for (int j = 1; j <= i; j++)
        {
            printf("#");
        }

        printf("\n");
    }
    return 0;
}