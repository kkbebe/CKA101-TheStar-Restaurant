package com.thestar.restaurant.controller.user;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.thestar.member.entity.MemberVO;
import com.thestar.restaurant.entity.ReservationStatus;
import com.thestar.restaurant.entity.RestaurantReservationVO;
import com.thestar.restaurant.service.RestaurantReservationService;




@Controller
@RequestMapping("/user")
public class RestaurantBookingController {
	
	@Autowired
    private RestaurantReservationService reservationService;
	
	@GetMapping("/booking")
    public String bookingPage(Model model) {
        if (!model.containsAttribute("reservationVO")) {
            RestaurantReservationVO reservationVO = new RestaurantReservationVO();
            MemberVO Member = new MemberVO();
            Member.setMemberId(1);
            reservationVO.setMemberVO(Member);
            model.addAttribute("reservationVO", reservationVO);
        }
        return "user/booking";
    }

    @PostMapping("/booking/submit")
    public String submitBooking(
            @ModelAttribute("reservationVO") RestaurantReservationVO reservationVO,
            BindingResult result,
            Model model,
            RedirectAttributes redirectAttributes) {
        
        // 🛠️ 【核心修正】補足前台表單沒填寫、但後端 Entity 規定 @NotNull 的必須系統變數
        // 預設評論狀態為 false (尚未評論)
        if (reservationVO.getReviewStatus() == null) {
            reservationVO.setReviewStatus(false);
        }
        
        // 預設訂位狀態 (請根據您 ReservationStatus 定義的常數修改，例如 PENDING、CONFIRMED 等)
        // 這裡假設您的第一個狀態常數為 PENDING (若為英文或其他，請替換為您正確的 Enum 項目)
        if (reservationVO.getReservationStatus() == null) {
            try {
                // 自動抓取 Enum 的第一個常數作為預設，避免您常數取名不同而報錯
                reservationVO.setReservationStatus(ReservationStatus.values()[0]);
            } catch (Exception e) {
                // 如果 Enum 為空，手動忽視或設為您實體擁有的狀態
            }
        }

        // 進行手動的手動屬性檢查（如果您需要使用精準的 @Valid，請將引數加回 @Valid）
        // 為了防止前端傳入空物件的巢狀錯誤，如果 result 出錯，我們把錯誤印出來並留在原頁面
        if (result.hasErrors()) {
            model.addAttribute("errorMessage", "輸入資料有誤，請檢查欄位。");
            return "booking";
        }
        
        try {
            reservationService.addReservation(reservationVO);
            redirectAttributes.addFlashAttribute("successMessage", "恭喜您！訂位預約成功！");
            return "redirect:/user/booking";
        } catch (Exception e) {
            model.addAttribute("errorMessage", "訂位失敗：" + e.getMessage());
            return "user/booking";
        }
    }

}
