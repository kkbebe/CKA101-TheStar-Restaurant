package com.thestar.restaurant.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import com.thestar.restaurant.entity.BusinessHoursVO;
import com.thestar.restaurant.service.BusinessHoursService;
import jakarta.validation.Valid;
import java.util.List;

@Controller
@RequestMapping("/backend/businesshours")
public class BusinessHoursController {

    @Autowired
    private BusinessHoursService bhService;

    // 時段列表
    @GetMapping("/list")
    public String list(Model model) {
        List<BusinessHoursVO> list = bhService.getAll();
        model.addAttribute("bhList", list);
        return "backend/businesshours/list";
    }

    // 前往新增
    @GetMapping("/addPage")
    public String addPage(Model model) {
        model.addAttribute("businessHoursVO", new BusinessHoursVO());
        return "backend/businesshours/add";
    }

    // 儲存時段
    @PostMapping("/save")
    public String save(@Valid @ModelAttribute("businessHoursVO") BusinessHoursVO bhVO, BindingResult result) {
        if (result.hasErrors()) {
            return "backend/businesshours/add";
        }
        bhService.addBusinessHours(bhVO);
        return "redirect:/backend/businesshours/list";
    }

    // 前往修改
    @GetMapping("/editPage")
    public String editPage(@RequestParam("sessionId") Integer sessionId, Model model) {
        BusinessHoursVO bhVO = bhService.getOneBusinessHours(sessionId);
        model.addAttribute("businessHoursVO", bhVO);
        return "backend/businesshours/edit";
    }

    // 刪除時段
    @PostMapping("/delete")
    public String delete(@RequestParam("sessionId") Integer sessionId) {
        bhService.deleteBusinessHours(sessionId);
        return "redirect:/backend/businesshours/list";
    }
}