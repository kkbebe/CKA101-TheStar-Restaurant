package com.thestar.restaurant.service;

import java.sql.Date;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.thestar.restaurant.entity.AvailableTableId;
import com.thestar.restaurant.entity.AvailableTableVO;
import com.thestar.restaurant.repository.AvailableTableRepository;

@Service
public class AvailableTableService {

    @Autowired
    AvailableTableRepository repository;

    /*
     * 複合主鍵的 Service 寫法：
     * 所有需要傳入 id 的地方，改成傳入 AvailableTableId 物件，
     * 或分別傳入 date + sessionId，再在 Service 內組成 AvailableTableId
     */

    public void addAvailableTable(AvailableTableVO availableTableVO) {
        repository.save(availableTableVO);
    }

    public void updateAvailableTable(AvailableTableVO availableTableVO) {
        repository.save(availableTableVO);
    }

    // 刪除：傳入兩個主鍵欄位，組成 AvailableTableId 後再刪除
    public void deleteAvailableTable(Date date, Integer sessionId) {
        AvailableTableId id = new AvailableTableId(date, sessionId);
        if (repository.existsById(id))
            repository.deleteById(id);
    }

    // 查單筆：傳入兩個主鍵欄位，組成 AvailableTableId 後查詢
    public AvailableTableVO getOneAvailableTable(Date date, Integer sessionId) {
        AvailableTableId id = new AvailableTableId(date, sessionId);
        Optional<AvailableTableVO> optional = repository.findById(id);
        return optional.orElse(null);
    }

    // 查全部
    public List<AvailableTableVO> getAll() {
        return repository.findAll();
    }

    // 查某天的所有時段餘量（前台選位用）
    public List<AvailableTableVO> getByDate(Date date) {
        return repository.findById_Date(date);
    }

    // 查某天還有大桌的時段
    public List<AvailableTableVO> getAvailableLargeTables(Date date) {
        return repository.findAvailableLargeTablesByDate(date);
    }

    // 查某天還有小桌的時段
    public List<AvailableTableVO> getAvailableSmallTables(Date date) {
        return repository.findAvailableSmallTablesByDate(date);
    }

    // 訂位成功後，扣減大桌數量
    public void decreaseLargeTableCount(Date date, Integer sessionId) {
        AvailableTableVO vo = getOneAvailableTable(date, sessionId);
        if (vo != null && vo.getLargeTableCount() > 0)
            repository.updateLargeTableCount(date, sessionId, vo.getLargeTableCount() - 1);
    }

    // 訂位成功後，扣減小桌數量
    public void decreaseSmallTableCount(Date date, Integer sessionId) {
        AvailableTableVO vo = getOneAvailableTable(date, sessionId);
        if (vo != null && vo.getSmallTableCount() > 0)
            repository.updateSmallTableCount(date, sessionId, vo.getSmallTableCount() - 1);
    }

    // 取消訂位後，歸還大桌數量
    public void restoreLargeTableCount(Date date, Integer sessionId) {
        AvailableTableVO vo = getOneAvailableTable(date, sessionId);
        if (vo != null)
            repository.updateLargeTableCount(date, sessionId, vo.getLargeTableCount() + 1);
    }

    // 取消訂位後，歸還小桌數量
    public void restoreSmallTableCount(Date date, Integer sessionId) {
        AvailableTableVO vo = getOneAvailableTable(date, sessionId);
        if (vo != null)
            repository.updateSmallTableCount(date, sessionId, vo.getSmallTableCount() + 1);
    }
}
