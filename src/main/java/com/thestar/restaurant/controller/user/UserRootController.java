package com.thestar.restaurant.controller.user;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;



@Controller
public class UserRootController {
	
	@GetMapping("/")
	public String root() {
	    return "user/index"; // 當使用者輸入 localhost:8080 時，自動幫他轉址到 /user/index
	}

}
