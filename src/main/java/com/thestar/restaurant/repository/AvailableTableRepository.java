package com.thestar.restaurant.repository;

import java.sql.Date;
import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.transaction.annotation.Transactional;

import com.thestar.restaurant.entity.AvailableTableId;
import com.thestar.restaurant.entity.AvailableTableVO;

// https://docs.spring.io/spring-data/jpa/docs/current/reference/html/
/*
 * 複合主鍵的 Repository：泛型第二個型別填 AvailableTableId（不再是 Integer）
 *
 *   JpaRepository<AvailableTableVO, AvailableTableId>
 *                  └─ Entity 型別    └─ 主鍵型別（改成複合主鍵類別）
 *
 * 繼承的方法也會跟著改變，例如：
 *   findById(AvailableTableId id)
 *   deleteById(AvailableTableId id)
 *
 * 方法命名查詢存取 @EmbeddedId 內部欄位，規則是：
 *   id_欄位名稱（用底線分隔 EmbeddedId 屬性名稱 和 內部欄位名稱）
 *   例：id.date → findById_Date(...)
 */	
public interface AvailableTableRepository extends JpaRepository<AvailableTableVO, AvailableTableId> {

    // 查詢某一天的所有時段餘量（前台選位、後台查看用）
    // id_date → 對應 AvailableTableId 裡的 date 欄位
    List<AvailableTableVO> findById_Date(Date date);

    // 查詢某時段在某天的餘量（訂位前確認是否有位置）
    Optional<AvailableTableVO> findById_DateAndId_SessionId(Date date, Integer sessionId);

    // 更新指定日期+時段的大桌數量（訂位成功後扣桌）
    @Transactional
    @Modifying
    @Query("update AvailableTableVO set largeTableCount = ?3 where id.date = ?1 and id.sessionId = ?2")
    void updateLargeTableCount(Date date, Integer sessionId, int newCount);

    // 更新指定日期+時段的小桌數量
    @Transactional
    @Modifying
    @Query("update AvailableTableVO set smallTableCount = ?3 where id.date = ?1 and id.sessionId = ?2")
    void updateSmallTableCount(Date date, Integer sessionId, int newCount);

    // 查詢某天還有大桌剩餘的時段（>0 才顯示）
    @Query("from AvailableTableVO where id.date = ?1 and largeTableCount > 0")
    List<AvailableTableVO> findAvailableLargeTablesByDate(Date date);

    // 查詢某天還有小桌剩餘的時段
    @Query("from AvailableTableVO where id.date = ?1 and smallTableCount > 0")
    List<AvailableTableVO> findAvailableSmallTablesByDate(Date date);
}
