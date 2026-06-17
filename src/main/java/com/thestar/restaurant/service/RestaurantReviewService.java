package com.thestar.restaurant.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.thestar.restaurant.entity.RestaurantReviewVO;
import com.thestar.restaurant.repository.RestaurantReviewRepository;

@Service
public class RestaurantReviewService {

    @Autowired
    RestaurantReviewRepository repository;

    public void addReview(RestaurantReviewVO reviewVO) {
        repository.save(reviewVO);
    }

    public void updateReview(RestaurantReviewVO reviewVO) {
        repository.save(reviewVO);
    }

    public void deleteReview(Integer reviewId) {
        if (repository.existsById(reviewId))
            repository.deleteById(reviewId);
    }

    public RestaurantReviewVO getOneReview(Integer reviewId) {
        Optional<RestaurantReviewVO> optional = repository.findById(reviewId);
        return optional.orElse(null);
    }

    // 取得全部評論（後台管理）
    public List<RestaurantReviewVO> getAll() {
        return repository.findAllOrderByReviewIdDesc();
    }

    // 查某會員的所有評論
    public List<RestaurantReviewVO> getByMemberId(Integer memberId) {
        return repository.findByMemberId(memberId);
    }

    // 查某筆訂位的評論（確認是否已評論過）
    public RestaurantReviewVO getByReservationId(Integer reservationId) {
        return repository.findByRestaurantReservationVO_ReservationId(reservationId);
    }

    // 查高星評論（首頁精選）
    public List<RestaurantReviewVO> getHighStarReviews(int minStars) {
        return repository.findByMinStars(minStars);
    }

    // 取得平均星等（首頁展示）
    public Double getAverageStars() {
        return repository.findAverageStars();
    }
}
