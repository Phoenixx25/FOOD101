{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "193fb600-665c-432b-bce9-5da7b586c87c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3fe18458-1e37-483d-88b5-cad2ccddfc85",
   "metadata": {},
   "outputs": [],
   "source": [
    "def matrix_operation(arr1,arr2,op)\n",
    "   if op==\"dot\":\n",
    "       if arr1.shape==arr2.shape:\n",
    "           dimensions = arr1.shape\n",
    "           rows, columns = dimensions\n",
    "           for i in range(0,rows):\n",
    "               for j in range(0,columns):\n",
    "                   dot+=arr1[i][j]*arr2[i][j]\n",
    "           return dot\n",
    "       else:\n",
    "           print(\"dot product not possible\")\n",
    "           return\n",
    "  elif op==\"matrix\":\n",
    "       dimensions1 = arr1.shape\n",
    "       r1, c1 = dimensions1 \n",
    "       dimensions2 = arr2.shape\n",
    "       r2, c2 = dimensions2\n",
    "       if c1==r2:\n",
    "           res = [[0] * c2 for _ in range(r1)]\n",
    "           for i in range(r1):\n",
    "              for j in range(c2):\n",
    "                for k in range(c1):\n",
    "                   res[i][j] += m1[i][k] * m2[k][j]\n",
    "\n",
    "      return res\n",
    "      else:\n",
    "         print(\"matrix multiplication not possible\")\n",
    "         return\n",
    "       \n",
    "    \n",
    "   "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (food101)",
   "language": "python",
   "name": "food101"
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
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
