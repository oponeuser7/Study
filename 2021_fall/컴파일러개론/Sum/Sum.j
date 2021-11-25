.class public Sum

.super java/lang/Object
.method public <init>()V
aload_0
invokenonvirtual java/lang/Object/<init>()V
return
.end method

;sum function
.method public static sum(I)I
.limit stack 32
.limit locals 8
ldc 1
istore_1 
ldc 2
istore_2 
ldc 100
istore_3
Loop: 
iload_1
iload_2
iadd
istore_1
iinc 2 1
iload_2
iload_3
ifne Loop 
iload_1
;write your code

ireturn
.end method

.method public static main([Ljava/lang/String;)V
.limit stack 32
.limit locals 8
ldc 1
istore 0
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 0
invokestatic Sum/sum(I)I
invokevirtual java/io/PrintStream/println(I)V
return
.end method
