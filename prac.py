{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "C=2\n",
    "def circle():\n",
    "    X in C\n",
    "    X=3.14*C*C\n",
    "    print(\"X\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "ename": "UnboundLocalError",
     "evalue": "local variable 'X' referenced before assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mUnboundLocalError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-16-c5a6408645bd>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mcircle\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-14-861c2c898d2a>\u001b[0m in \u001b[0;36mcircle\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mC\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mcircle\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[0mX\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mC\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m     \u001b[0mX\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m3.14\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mC\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mC\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"X\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mUnboundLocalError\u001b[0m: local variable 'X' referenced before assignment"
     ]
    }
   ],
   "source": [
    "circle()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.141592653589793"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=pi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.141592653589793"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "input of r 2.2\n",
      "15.205308443374602\n"
     ]
    }
   ],
   "source": [
    "x=pi\n",
    "r=float(input(\"input of r \"))\n",
    "y=x*r*r\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Prime numbers between 990 and 1000 are:\n",
      "991\n",
      "997\n"
     ]
    }
   ],
   "source": [
    "lower = 990\n",
    "upper=1000\n",
    "print(\"Prime numbers between\", lower, \"and\",upper ,\"are:\")\n",
    "\n",
    "for num in range(lower, upper + 1):\n",
    "   # all prime numbers are greater than 1\n",
    "   if num > 1:\n",
    "       for i in range(2, num):\n",
    "           if (num % i) == 0:\n",
    "               break\n",
    "       else:\n",
    "           print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "a=10\n",
    "b=100\n",
    "def range (a,b):\n",
    "    for y in (a,b):\n",
    "        c=0\n",
    "        for x in range(a,b+1):\n",
    "            if(y%x==0):\n",
    "                c=c+1\n",
    "        if(c==2):\n",
    "            print(\"prime number\")\n",
    "        else:\n",
    "            print(\"not prime\")\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "range() missing 2 required positional arguments: 'a' and 'b'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-29-5bcbe005bf48>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: range() missing 2 required positional arguments: 'a' and 'b'"
     ]
    }
   ],
   "source": [
    "range()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "start=1\n",
    "end=100\n",
    "def compute():\n",
    "    if x in j:\n",
    "        for j in range(start, end):\n",
    "              for y in j:\n",
    "                c=0\n",
    "                if(y%x==0):\n",
    "                    c=c+1\n",
    "                    if(c==2):\n",
    "                        print(\"prime number\")\n",
    "                    else:\n",
    "                        print(\"not prime\")\n",
    "       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "ename": "UnboundLocalError",
     "evalue": "local variable 'j' referenced before assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mUnboundLocalError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-41-bab79c2bc632>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mcompute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-40-f55d80c0c756>\u001b[0m in \u001b[0;36mcompute\u001b[1;34m()\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mend\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m100\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mcompute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m     \u001b[1;32mif\u001b[0m \u001b[0mx\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mj\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mj\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstart\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m               \u001b[1;32mfor\u001b[0m \u001b[0my\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mj\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mUnboundLocalError\u001b[0m: local variable 'j' referenced before assignment"
     ]
    }
   ],
   "source": [
    "compute()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "argument of type 'int' is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-46-1dc5448a5e76>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      6\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m             \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"not prime\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m \u001b[0mcompute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-46-1dc5448a5e76>\u001b[0m in \u001b[0;36mcompute\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0my\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mcompute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[1;32mif\u001b[0m \u001b[0mx\u001b[0m \u001b[1;32min\u001b[0m \u001b[0my\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m         \u001b[1;32mif\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m%\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m==\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m             \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"prime\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: argument of type 'int' is not iterable"
     ]
    }
   ],
   "source": [
    "y=10\n",
    "def compute():\n",
    "    if x in y:\n",
    "        if(x%y==0):\n",
    "            print(\"prime\")\n",
    "        else:\n",
    "            print(\"not prime\")\n",
    "compute()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "How many terms? 1\n",
      "Fibonacci sequence upto 1 :\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "# Program to display the Fibonacci sequence up to n-th term\n",
    "nterms = int(input(\"How many terms? \"))\n",
    "# first two terms\n",
    "n1, n2 = 0, 1\n",
    "count = 0\n",
    "# check if the number of terms is valid\n",
    "if nterms <= 0:\n",
    "   print(\"Please enter a positive integer\")\n",
    "elif nterms == 1:\n",
    "   print(\"Fibonacci sequence upto\",nterms,\":\")\n",
    "   print(n1)\n",
    "else:\n",
    "   print(\"Fibonacci sequence:\")\n",
    "   while count < nterms:\n",
    "       print(n1)\n",
    "       nth = n1 + n2\n",
    "       # update values\n",
    "       n1 = n2\n",
    "       n2 = nth\n",
    "       count += 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter number5\n",
      "odd\n"
     ]
    }
   ],
   "source": [
    "num=int(input(\"enter number\"))\n",
    "if(num%2==0):\n",
    "        print(\"even\")\n",
    "else:\n",
    "        print(\"odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=[1,-1,3,4,-2]\n",
    "def compute():\n",
    "    if Y in x:\n",
    "        if(x>0):\n",
    "            print(\"positive\")\n",
    "        else:\n",
    "            print(\"negative\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Y' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-64-bab79c2bc632>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mcompute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-63-05c83af4fb72>\u001b[0m in \u001b[0;36mcompute\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mcompute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[1;32mif\u001b[0m \u001b[0mY\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m         \u001b[1;32mif\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m>\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m             \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"positive\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'Y' is not defined"
     ]
    }
   ],
   "source": [
    "compute()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "even 3\n",
      "odd 3\n"
     ]
    }
   ],
   "source": [
    "list1 = [2,8,15,-16,13,27]\n",
    "even,odd= 0,0\n",
    "for num in list1:\n",
    "    if (num%2==0):\n",
    "        even +=1\n",
    "    else:\n",
    "        odd +=1\n",
    "print(\"even\",even)\n",
    "print(\"odd\",odd)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Positive numbers : 3\n"
     ]
    }
   ],
   "source": [
    "list1 = [1,-9,15,-16,13]\n",
    "pos= 0\n",
    "for num in list1:\n",
    "    if num >= 0:\n",
    "        pos += 1\n",
    "print(\"Positive numbers :\",pos)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Positive numbers :  3\n"
     ]
    }
   ],
   "source": [
    "list1 = [1,-9,15,-16,13]\n",
    "pos_count= 0\n",
    "for num in list1:\n",
    "    if num >= 0:\n",
    "        pos_count += 1\n",
    "print(\"Positive numbers : \", pos_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "odd 2\n"
     ]
    }
   ],
   "source": [
    "list1 = [2,8,15,-16,13]\n",
    "odd=0\n",
    "for num in(list1):\n",
    "    if(num%2!=0):\n",
    "        odd +=1\n",
    "print(\"odd\",odd)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "ename": "RecursionError",
     "evalue": "maximum recursion depth exceeded",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mRecursionError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-128-65e9786e550f>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mstart\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mend\u001b[0m \u001b[1;33m=\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mfor\u001b[0m \u001b[0mnum\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstart\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[1;31m# checking condition\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mnum\u001b[0m \u001b[1;33m>=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-28-106951c76068>\u001b[0m in \u001b[0;36mrange\u001b[1;34m(a, b)\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0my\u001b[0m \u001b[1;32min\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[0mc\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m         \u001b[1;32mfor\u001b[0m \u001b[0mx\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      7\u001b[0m             \u001b[1;32mif\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m%\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m==\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m                 \u001b[0mc\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mc\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "... last 1 frames repeated, from the frame below ...\n",
      "\u001b[1;32m<ipython-input-28-106951c76068>\u001b[0m in \u001b[0;36mrange\u001b[1;34m(a, b)\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0my\u001b[0m \u001b[1;32min\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[0mc\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m         \u001b[1;32mfor\u001b[0m \u001b[0mx\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      7\u001b[0m             \u001b[1;32mif\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m%\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m==\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m                 \u001b[0mc\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mc\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mRecursionError\u001b[0m: maximum recursion depth exceeded"
     ]
    }
   ],
   "source": [
    "start,end =-3,4\n",
    "for num in range(start, end + 1):\n",
    "     \n",
    "    # checking condition\n",
    "    if num >= 0:\n",
    "        print(num, end = \" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
