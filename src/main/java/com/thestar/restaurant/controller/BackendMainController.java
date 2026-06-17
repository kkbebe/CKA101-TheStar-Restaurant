package com.thestar.restaurant.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class BackendMainController {

    // 讓訪問 http://localhost:8080/backend 時導向總首頁
    @GetMapping("/backend")
    public String backendIndex() {
        return "backend/index";
    }
}