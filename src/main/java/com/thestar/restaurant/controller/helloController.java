package com.thestar.restaurant.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController // 1. 告訴 Spring 這是一個 REST 控制器
public class helloController {

    // 2. 設定路由，當訪問 http://localhost:8080/hello 時會觸發這個方法
    @GetMapping("/hello")
    public String sayHello() {
        return "哈囉！歡迎光臨 The Star 餐廳！"; 
    }

    // 3. 進階：還可以帶參數，例如 http://localhost:8080/greet?name=艾倫
    @GetMapping("/greet")
    public String greetUser(@RequestParam(value = "name", defaultValue = "貴賓") String name) {
        return "哈囉 " + name + "，祝您用餐愉快！";
    }
}