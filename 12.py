import os

OUTPUT_DIR = "temp_layout_files"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_file(sub_path, file_name, content):
    target_dir = os.path.join(OUTPUT_DIR, sub_path)
    os.makedirs(target_dir, exist_ok=True)
    full_path = os.path.join(target_dir, file_name)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"已生成整合檔案: {full_path}")

# =====================================================================
# 0. 公用元件 (Fragment) - 包含美化 CSS、側邊欄、頂部導航
# =====================================================================
common_sidebar_html = """
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:fragment="common-head(title)">
    <meta charset="UTF-8">
    <title th:text="${title}">The Star 後台管理</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { display: flex; min-hieght: 100vh; background-color: #f8f9fa; overflow-x: hidden; }
        .sidebar { width: 260px; background-color: #212529; color: #fff; min-height: 100vh; transition: all 0.3s; }
        .sidebar .logo { padding: 20px; font-size: 1.25rem; font-weight: bold; text-align: center; background-color: #1a1d20; border-bottom: 1px solid #343a40; }
        .sidebar .nav-link { color: #dee2e6; padding: 12px 20px; display: flex; align-items: center; gap: 12px; transition: all 0.2s; border-radius: 4px; margin: 4px 8px; }
        .sidebar .nav-link:hover, .sidebar .nav-link.active { background-color: #0d6efd; color: #fff; text-decoration: none; }
        .main-content { flex: 1; display: flex; flex-direction: column; min-width: 0; }
        .top-navbar { background-color: #fff; padding: 15px 30px; border-bottom: 1px solid #dee2e6; display: flex; justify-content: space-between; align-items: center; }
        .page-body { padding: 30px; flex: 1; }
        .card { border: none; box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075); border-radius: 8px; }
    </style>
</head>
<body>

    <div th:fragment="sidebar(activePage)" class="sidebar">
        <div class="logo">
            <i class="fa-solid fa-star text-warning me-2"></i>The Star 後台系統
        </div>
        <div class="nav flex-column mt-3">
            <a href="/backend" class="nav-link" th:classappend="${activePage == 'home'} ? 'active'">
                <i class="fa-solid fa-gauge fa-fw"></i> 後台控制台
            </a>
            <a href="/backend/table/list" class="nav-link" th:classappend="${activePage == 'table'} ? 'active'">
                <i class="fa-solid fa-table fa-fw"></i> 桌型管理設定
            </a>
            <a href="/backend/businesshours/list" class="nav-link" th:classappend="${activePage == 'hours'} ? 'active'">
                <i class="fa-solid fa-clock fa-fw"></i> 營業時段管理
            </a>
            <a href="/backend/menu/list" class="nav-link" th:classappend="${activePage == 'menu'} ? 'active'">
                <i class="fa-solid fa-utensils fa-fw"></i> 餐廳菜單管理
            </a>
            <a href="/backend/reservation/list" class="nav-link" th:classappend="${activePage == 'reservation'} ? 'active'">
                <i class="fa-solid fa-calendar-check fa-fw"></i> 預約紀錄管理
            </a>
            <a href="/backend/review/list" class="nav-link" th:classappend="${activePage == 'review'} ? 'active'">
                <i class="fa-solid fa-comment-dots fa-fw"></i> 顧客評論管理
            </a>
        </div>
    </div>

    <div th:fragment="topbar(pageTitle)" class="top-navbar">
        <h4 class="m-0 fw-bold text-secondary" th:text="${pageTitle}">分頁標題</h4>
        <div class="d-flex align-items-center gap-3">
            <span class="text-muted"><i class="fa-solid fa-user-shield me-1"></i> 管理員 (Admin)</span>
            <a href="/" class="btn btn-outline-secondary btn-sm"><i class="fa-solid fa-house"></i> 回前台首頁</a>
        </div>
    </div>

</body>
</html>
"""

# =====================================================================
# 1. 後台總首頁 (index.html) -> 對應 /backend
# =====================================================================
index_html = """
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="~{backend/common_sidebar :: common-head('The Star 後台管理主頁')}"></head>
<body>
    <div th:replace="~{backend/common_sidebar :: sidebar('home')}"></div>
    
    <div class="main-content">
        <div th:replace="~{backend/common_sidebar :: topbar('後台控制台首頁')}"></div>
        
        <div class="page-body">
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="card p-4 bg-primary text-white">
                        <h5><i class="fa-solid fa-calendar-check me-2"></i> 快速處理預約</h5>
                        <p class="fs-6 opacity-75">查看與審核今日顧客訂位</p>
                        <a href="/backend/reservation/list" class="btn btn-light btn-sm mt-2 text-primary fw-bold">前往管理</a>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card p-4 bg-success text-white">
                        <h5><i class="fa-solid fa-utensils me-2"></i> 菜單品項調整</h5>
                        <p class="fs-6 opacity-75">上架新菜色、調整餐點價格</p>
                        <a href="/backend/menu/list" class="btn btn-light btn-sm mt-2 text-success fw-bold">前往管理</a>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card p-4 bg-dark text-white">
                        <h5><i class="fa-solid fa-comment-dots me-2"></i> 最新顧客評價</h5>
                        <p class="fs-6 opacity-75">控管、維護餐廳商譽評論</p>
                        <a href="/backend/review/list" class="btn btn-light btn-sm mt-2 text-dark fw-bold">前往管理</a>
                    </div>
                </div>
            </div>
            
            <div class="card mt-4 p-4">
                <h5 class="fw-bold mb-3"><i class="fa-solid fa-bullhorn text-warning me-2"></i>系統說明</h5>
                <p>歡迎登入 **The Star 餐廳後台管理系統**。請點選左側導航欄位，對餐廳的基礎硬體（桌型、營業時間）、前台展示（菜單）以及營運數據（預約、評論）進行即時管理與維護。</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

# =====================================================================
# 2. 整合後的 5 個功能清單網頁
# =====================================================================
table_list_html = """
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="~{backend/common_sidebar :: common-head('桌型管理設定')}"></head>
<body>
    <div th:replace="~{backend/common_sidebar :: sidebar('table')}"></div>
    <div class="main-content">
        <div th:replace="~{backend/common_sidebar :: topbar('桌型分佈與數量設定')}"></div>
        <div class="page-body">
            <div class="card p-4">
                <div class="d-flex justify-content-between align-items-center mb-3">
                    <h5 class="m-0 fw-bold"><i class="fa-solid fa-list me-2"></i>現有桌型列表</h5>
                    <a href="/backend/table/addPage" class="btn btn-primary"><i class="fa-solid fa-plus me-1"></i>定義新規格</a>
                </div>
                <table class="table table-hover table-bordered align-middle">
                    <thead class="table-light">
                        <tr>
                            <th>桌型人數規格 (Table Type)</th>
                            <th>該規格總桌數 (Table Count)</th>
                            <th width="180">操作</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr th:each="table : ${tableList}">
                            <td class="fw-bold text-primary" th:text="${table.tableType} + ' 人桌'">2 人桌</td>
                            <td th:text="${table.tableCount} + ' 桌'">5 桌</td>
                            <td>
                                <a th:href="@{/backend/table/editPage(tableType=${table.tableType})}" class="btn btn-warning btn-sm"><i class="fa-solid fa-pen"></i> 修改</a>
                                <form th:action="@{/backend/table/delete}" method="post" style="display:inline;" onsubmit="return confirm('確定要刪除嗎？');">
                                    <input type="hidden" name="tableType" th:value="${table.tableType}">
                                    <button type="submit" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash"></i> 刪除</button>
                                </form>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>
"""

bh_list_html = """
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="~{backend/common_sidebar :: common-head('營業時段管理')}"></head>
<body>
    <div th:replace="~{backend/common_sidebar :: sidebar('hours')}"></div>
    <div class="main-content">
        <div th:replace="~{backend/common_sidebar :: topbar('餐廳營業時段配置')}"></div>
        <div class="page-body">
            <div class="card p-4">
                <div class="d-flex justify-content-between align-items-center mb-3">
                    <h5 class="m-0 fw-bold"><i class="fa-solid fa-clock me-2"></i>營業時段列表</h5>
                    <a href="/backend/businesshours/addPage" class="btn btn-primary"><i class="fa-solid fa-plus me-1"></i>新增時段</a>
                </div>
                <table class="table table-striped table-bordered align-middle">
                    <thead class="table-light">
                        <tr>
                            <th>時段流水號 (Session ID)</th>
                            <th>開始時間 (Start)</th>
                            <th>結束時間 (End)</th>
                            <th width="180">操作</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr th:each="bh : ${bhList}">
                            <td th:text="${bh.sessionId}">1</td>
                            <td class="text-success fw-bold" th:text="${bh.startTime}">11:30:00</td>
                            <td class="text-danger fw-bold" th:text="${bh.endTime}">14:00:00</td>
                            <td>
                                <a th:href="@{/backend/businesshours/editPage(sessionId=${bh.sessionId})}" class="btn btn-warning btn-sm"><i class="fa-solid fa-pen"></i> 修改</a>
                                <form th:action="@{/backend/businesshours/delete}" method="post" style="display:inline;" onsubmit="return confirm('確定要刪除此營業時段嗎？');">
                                    <input type="hidden" name="sessionId" th:value="${bh.sessionId}">
                                    <button type="submit" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash"></i> 刪除</button>
                                </form>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>
"""

menu_list_html = """
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="~{backend/common_sidebar :: common-head('餐廳菜單管理')}"></head>
<body>
    <div th:replace="~{backend/common_sidebar :: sidebar('menu')}"></div>
    <div class="main-content">
        <div th:replace="~{backend/common_sidebar :: topbar('菜單與線上餐點管理')}"></div>
        <div class="page-body">
            <div class="card p-4">
                <div class="d-flex justify-content-between align-items-center mb-3">
                    <h5 class="m-0 fw-bold"><i class="fa-solid fa-utensils me-2"></i>目前供應品項</h5>
                    <a href="/backend/menu/addPage" class="btn btn-success"><i class="fa-solid fa-plus me-1"></i>上架新餐點</a>
                </div>
                <table class="table table-bordered table-hover align-middle">
                    <thead class="table-light">
                        <tr>
                            <th>ID</th>
                            <th>縮圖</th>
                            <th>品項分類</th>
                            <th>餐點名稱</th>
                            <th>描述介紹</th>
                            <th>售價</th>
                            <th>排序</th>
                            <th width="160">操作</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr th:each="menu : ${menuList}">
                            <td th:text="${menu.itemId}">1</td>
                            <td>
                                <img th:if="${menu.imageUrl}" th:src="${menu.imageUrl}" width="55" height="40" class="img-thumbnail">
                                <span th:unless="${menu.imageUrl}" class="text-muted small">無圖片</span>
                            </td>
                            <td th:text="${menu.menuCategoryVO.categoryName}"><span class="badge bg-secondary">分類</span></td>
                            <td th:text="${menu.itemName}" class="fw-bold text-dark">經典牛排</td>
                            <td th:text="${menu.itemDesc}" class="text-muted small">描述...</td>
                            <td th:text="'$' + ${menu.price}" class="text-danger fw-bold">$350</td>
                            <td th:text="${menu.sortOrder}">10</td>
                            <td>
                                <a th:href="@{/backend/menu/editPage(itemId=${menu.itemId})}" class="btn btn-warning btn-sm"><i class="fa-solid fa-pen"></i></a>
                                <form th:action="@{/backend/menu/delete}" method="post" style="display:inline;" onsubmit="return confirm('確定要刪除此品項嗎？');">
                                    <input type="hidden" name="itemId" th:value="${menu.itemId}">
                                    <button type="submit" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash"></i></button>
                                </form>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>
"""

reservation_list_html = """
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="~{backend/common_sidebar :: common-head('預約紀錄管理')}"></head>
<body>
    <div th:replace="~{backend/common_sidebar :: sidebar('reservation')}"></div>
    <div class="main-content">
        <div th:replace="~{backend/common_sidebar :: topbar('客戶訂位預約控制中心')}"></div>
        <div class="page-body">
            <div class="card p-4">
                <h5 class="fw-bold mb-3"><i class="fa-solid fa-book-bookmark me-2"></i>預約紀錄報表</h5>
                <table class="table table-hover table-bordered align-middle">
                    <thead class="table-light">
                        <tr>
                            <th>預約編號</th>
                            <th>會員 ID</th>
                            <th>預約日期</th>
                            <th>訂位時段 (Session)</th>
                            <th>特殊需求備註</th>
                            <th>目前狀態</th>
                            <th width="200">狀態操作動作</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr th:each="res : ${reservationList}">
                            <td th:text="${res.reservationId}">100</td>
                            <td th:text="${res.memberVO}">Member</td>
                            <td th:text="${res.date}" class="fw-bold">2026-06-15</td>
                            <td th:text="${res.businessHoursVO.startTime} + ' ~ ' + ${res.businessHoursVO.endTime}">12:00~14:00</td>
                            <td th:text="${res.reservationRequest}" class="text-muted small">無</td>
                            <td>
                                <span th:if="${res.reservationStatus.name() == 'BOOKED'}" class="badge bg-primary p-2">已預約</span>
                                <span th:if="${res.reservationStatus.name() == 'FINISHED'}" class="badge bg-success p-2">已就餐</span>
                                <span th:if="${res.reservationStatus.name() == 'CANCELED'}" class="badge bg-danger p-2">已取消</span>
                            </td>
                            <td>
                                <div th:if="${res.reservationStatus.name() == 'BOOKED'}">
                                    <form th:action="@{/backend/reservation/updateStatus}" method="post" style="display:inline;">
                                        <input type="hidden" name="reservationId" th:value="${res.reservationId}">
                                        <input type="hidden" name="status" value="FINISHED">
                                        <button type="submit" class="btn btn-success btn-sm"><i class="fa-solid fa-check"></i> 結案就餐</button>
                                    </form>
                                    <form th:action="@{/backend/reservation/updateStatus}" method="post" style="display:inline;">
                                        <input type="hidden" name="reservationId" th:value="${res.reservationId}">
                                        <input type="hidden" name="status" value="CANCELED">
                                        <button type="submit" class="btn btn-outline-danger btn-sm"> 取消</button>
                                    </form>
                                </div>
                                <span th:unless="${res.reservationStatus.name() == 'BOOKED'}" class="text-muted small">無可用操作</span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>
"""

review_list_html = """
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head th:replace="~{backend/common_sidebar :: common-head('顧客評論管理')}"></head>
<body>
    <div th:replace="~{backend/common_sidebar :: sidebar('review')}"></div>
    <div class="main-content">
        <div th:replace="~{backend/common_sidebar :: topbar('顧客用餐評論維護')}"></div>
        <div class="page-body">
            <div class="card p-4">
                <h5 class="fw-bold mb-3"><i class="fa-solid fa-comments me-2"></i>顧客評分與反饋</h5>
                <table class="table table-striped table-bordered align-middle">
                    <thead class="table-light">
                        <tr>
                            <th>評論 ID</th>
                            <th>會員</th>
                            <th>對應預約單</th>
                            <th>星級評分</th>
                            <th>反饋評論內容</th>
                            <th width="100">操作</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr th:each="review : ${reviewList}">
                            <td th:text="${review.reviewId}">1</td>
                            <td th:text="${review.memberVO}">會員</td>
                            <td th:text="${review.restaurantReservationVO.reservationId}">1001</td>
                            <td>
                                <span th:each="i : ${#numbers.sequence(1, review.reviewStars)}" class="text-warning">★</span>
                            </td>
                            <td th:text="${review.reviewContent}" class="text-dark small">內容...</td>
                            <td>
                                <form th:action="@{/backend/review/delete}" method="post" onsubmit="return confirm('確定要審查並刪除這則評論嗎？');">
                                    <input type="hidden" name="reviewId" th:value="${review.reviewId}">
                                    <button type="submit" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash"></i> 刪除</button>
                                </form>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>
"""

create_file("", "common_sidebar.html", common_sidebar_html)
create_file("", "index.html", index_html)
create_file("table", "list.html", table_list_html)
create_file("businesshours", "list.html", bh_list_html)
create_file("menu", "list.html", menu_list_html)
create_file("reservation", "list.html", reservation_list_html)
create_file("review", "list.html", review_list_html)

print("\n=== 側邊欄整合版網頁已全部生成至: temp_layout_files 資料夾中 ===")