// IF-ELSE STATEMENT IN C

#include <stdio.h>

int main() {

    // Declare a variable
    int marks;

    // Take marks from the user
    printf("Enter your marks: ");
    scanf("%d", &marks);

    // Check if marks are 90 or above
    if (marks >= 90) {
        printf("Grade A");
    }

    // Check if marks are 75 or above
    else if (marks >= 75) {
        printf("Grade B");
    }

    // Check if marks are 50 or above
    else if (marks >= 50) {
        printf("Grade C");
    }

    // If none of the above conditions are true
    else {
        printf("Fail");
    }

    return 0; // End the program
}
