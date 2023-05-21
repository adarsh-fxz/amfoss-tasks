#include <cs50.h>
#include <stdio.h>

int main()
{
    long long int cardNum;
    int count = 0;

    printf("Enter card number: ");
    scanf("%lld", &cardNum);

    long long int cardNumTemp = cardNum;

    if (cardNumTemp < 0)
    {
        printf("INVALID\n");
        return 0;
    }

    else if (cardNumTemp == 0)
    {
        count = 1;
    }
    else
    {
        while (cardNumTemp != 0)
        {
            count++;
            cardNumTemp /= 10;
        }
    }

    if (count < 13 || count > 16 || count == 14)
    {
        printf("INVALID\n");
        return 0;
    }

    int sum = 0;
    int digitCount = 1;
    long long int temp = cardNum;
    while (temp != 0)
    {
        int digit = temp % 10;

        if (digitCount % 2 == 0)
        {
            digit *= 2;
            if (digit > 9)
            {
                digit = (digit % 10) + (digit / 10);
            }
        }

        sum += digit;
        temp /= 10;
        digitCount++;
    }

    if (sum % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    if (count == 15 && (cardNum / 10000000000000 == 34 || cardNum / 10000000000000 == 37))
    {
        printf("AMEX\n");
        return 0;
    }

    else if (count == 16)
    {

        if (cardNum / 100000000000000 == 51 || cardNum / 100000000000000 == 52 || cardNum / 100000000000000 == 53
            || cardNum / 100000000000000 == 54 || cardNum / 100000000000000 == 55)
        {
            printf("MASTERCARD\n");
            return 0;
        }
        else if (cardNum / 1000000000000000 == 4)
        {
            printf("VISA\n");
            return 0;
        }
        else
        {
            printf("INVALID\n");
            return 0;
        }
    }

    else if (count == 13 && cardNum / 1000000000000 == 4)
    {
        printf("VISA\n");
        return 0;
    }

    else
    {
        printf("INVALID\n");
        return 0;
    }
}