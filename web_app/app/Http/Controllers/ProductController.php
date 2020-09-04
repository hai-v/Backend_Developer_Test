<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Product;

class ProductController extends Controller
{
    /*
     * get all products
     * @return view of read with array of Product objects
     */
    public function read() {
        $products = Product::all();
        return view('read', compact('products'));
    } 
}
