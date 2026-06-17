package com.thestar.member.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "MEMBERS") // 隨便對應一個空表名稱即可
public class MemberVO implements java.io.Serializable {
    private static final long serialVersionUID = 1L;

    private Integer memberId;

    @Id
    @Column(name = "MEMBER_ID")
    public Integer getMemberId() {
        return memberId;
    }

    public void setMemberId(Integer memberId) {
        this.memberId = memberId;
    }

    // 為了讓 Thymeleaf 網頁在 ${review.memberVO} 時不會因為沒寫 toString() 而報錯
    @Override
    public String toString() {
        return "會員編號: " + memberId;
    }
}