char* convertToBase7(int num) {
    char arr[100];
    int i = 0;
    if (num == 0) {
        char* result = (char*)malloc(2*sizeof(char));
        result[0] = '0';
        result[1] = '\0';
        return result;
    }
    if (num < 0) {
        num = -num;
        while (num > 0) {
            arr[i] = num % 7 + '0';
            num /= 7;
            i++;
        }
        char* result = (char*)malloc((i + 2) * sizeof(char));
        int j = 0;
        int k = i - 1;
        result[j++] = '-';
        while (k >= 0) {
            result[j++] = arr[k--];
        }
        result[j] = '\0';
        return result;
    }
    while (num > 0) {
        arr[i] = num % 7 + '0';
        num /= 7;
        i++;
    }
    char* result = (char*)malloc((i + 1) * sizeof(char));
    int j;
    for (j = 0; j < i; j++) {
        result[j] = arr[i - 1 - j];
    }
    result[j] = '\0';
    return result;
}