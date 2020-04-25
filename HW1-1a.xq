for $b in doc("books.xml")//book 
order by xs:float($b/price) descending, $b/title ascending return $b/title


