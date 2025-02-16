<?php
error_reporting(0);
class ctf{
    public $name;
    public $power;
    public function __construct($name)
    {
        $this->name=$name;
        $this->power="users";
    }
    public function __destruct(){
        sha1($this->name);
    }

}
class web{
    public $evil;
public function __tostring(){
    $test=$this->evil;
    return $test();
}

}
class hacker{
    public $name;
    public function __invoke()
    {
    eval($this->name);      
    }
}
