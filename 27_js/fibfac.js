//Team lo :: Daniel Park, Yinwei
//SoftDev pd5
//K27 - Basic functions in JavaScript
//2025-01-06m


//JavaScript implementations of Day0 recursive Scheme functions

//factorial:
let fact = function(n){
    if(n == 0){
        return 1;
    } 
    return n * fact(n - 1)
}
//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
fact(1) == 1
fact(2) == 2
fact(3) == 6
fact(4) == 24
fact(5) == 120
fact(6) == 720
fact(7) == 5040
fact(10) == 3628800
//-----------------------------------------------------------------


//fib:
let fib = function(n){
    if(n < 2){
        return n;
    }
    return fib(n - 1) + fib(n - 2)
}
//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
fib(0) == 0
fib(1) == 1
fib(2) == 1
fib(3) == 2
fib(4) == 3
fib(5) == 5
fib(6) == 8
fib(10) == 55
//=================================================================
