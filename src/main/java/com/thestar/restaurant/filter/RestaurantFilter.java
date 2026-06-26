package com.thestar.restaurant.filter;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import org.hibernate.internal.build.AllowSysOut;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;
import java.io.IOException;

@Component
public class RestaurantFilter extends OncePerRequestFilter {
	
    /**
     * shouldNotFilter 提供了一個乾淨的方式來排除不需要過濾的路徑
     * 返回 true 代表「跳過過濾器」，返回 false 代表「執行過濾」
     */
    @Override
    protected boolean shouldNotFilter(HttpServletRequest request) throws ServletException {
        String uri = request.getRequestURI();
        
        // 排除登入頁面，避免無限重定向
        if (uri.endsWith("/login.html") || uri.endsWith("/login")) {
            return true;
        }
        
        // 受保護的範圍
        return !uri.contains("/booking")&&!uri.contains("/protected2");
    }


    @Override
    protected void doFilterInternal(HttpServletRequest request, 
                                    HttpServletResponse response, 
                                    FilterChain filterChain) throws ServletException, IOException {
    	
    	 /**
         * ●●取得當前路徑，從原本的request.getRequestURI(); 改用request.getServletPath();，原因說明如下:
         * 1)Spring MVC 的機制：當你使用(LoginHandler.java第36行) redirect:/... 時，Spring 會自動幫你加上當前的 context-path
         * 2)所以這邊不能用我們在Servlet技術中熟悉的request.getRequestURI();取得當前路徑，而必須要改採用request.getServletPath();
         * 3)否則在使用Spring MVC的redirect:/...的時候，context-path會重複出現兩次，造成application.properties第34行只能用預設的
         *   server.servlet.context-path=/ 之外，在Tomcat的執行環境下redirect:/...也會失效
         */
     // String uri = request.getRequestURI(); 
    	String uri = request.getServletPath();
        
    	// 取得 session
    	// Spring 的 OncePerRequestFilter 已經幫你轉好 HttpServletRequest 了，直接使用即可
        HttpSession session = request.getSession();

        // 1. 檢查使用者是否登入過
        Object account = session.getAttribute("account");

        // --- account如果為 null，代表此user未登入過  ---
        if (account == null) {
            // session存入當前路徑，以便登入後跳轉回此路徑
            session.setAttribute("location", uri);
            // 重定(導)向到登入頁
            response.sendRedirect(request.getContextPath() + "/login"); // --> com.IndexController_inSpringBoot.java 第16行
        } else {
            // 已登入，繼續下一個過濾器或 Controller
            filterChain.doFilter(request, response);
        }
    }
}
