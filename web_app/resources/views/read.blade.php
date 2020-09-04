<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Hai Vu - Backend Test</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    </head>
    <body>
        <table class="table table-bordered table-striped">
            <thead>
                <tr>
                    <th scope="col">Product Name</th>
                    <th scope="col">Total Available</th>
                </tr>
            </thead>
            <tbody>
                @foreach($products as $p)
                <tr>
                    <td>{{$p->productName}}</td>
                    <td>{{$p->totalAvailable}}</td>
                </tr>
                @endforeach
            </tbody>
        <table>
    </body>
</html>