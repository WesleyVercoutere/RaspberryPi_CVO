//An array is a collection of variables that are accessed with an index number, Arrays in C are zero indexed

int myInts[6];
int myPins[] = {2, 4, 8, 3, 6};
int mySensVals[6] = {2, 4, -8, 3, 2};
int intarray[] = {1, 2, 3, 4, 5};
double doublearray[] = {2.1, 2.3, 2.4, 2.5};
// int test[];        compilation error   storage size is not known

int tabel[3][5] = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}}; //3 rows 5 columns

// arrays of characters in apparte les samen met het String object

void setup() {

  Serial.begin(9600);

}

void loop() {

  Serial.println( myPins[1]);
  myPins[1] = 9;
  Serial.println( myPins[1]);

  Serial.println(tabel[2][3]);
  tabel[2][3] = 88;
  Serial.println(tabel[2][3]);

  Serial.println( mySensVals[0]);
  Serial.println( mySensVals[5]);   // where are we looking now?
  
  while (1);

}
