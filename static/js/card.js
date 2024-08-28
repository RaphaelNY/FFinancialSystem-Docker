document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card');
    let activeCard = null;

    cards.forEach(card => {
        // 左键点击事件：使卡片居中并放大，显示 .info 部分
        card.addEventListener('click', () => {
            if (activeCard) {
                // 如果有活动的卡片，先将其恢复
                activeCard.classList.remove('centered', 'show-info');
                cards.forEach(c => c.classList.remove('hidden'));
            }
            // 设定新活动卡片
            card.classList.add('centered', 'show-info'); // 添加 'show-info' 以显示 .info 部分
            cards.forEach(c => {
                if (c !== card) {
                    c.classList.add('hidden');  // 隐藏其他卡片
                }
            });
            activeCard = card;
        });

        // 右键点击事件：恢复卡片状态
        card.addEventListener('contextmenu', (e) => {
            e.preventDefault(); // 禁用右键菜单
            if (activeCard) {
                activeCard.classList.remove('centered', 'show-info'); // 移除 'centered' 和 'show-info'
                cards.forEach(c => c.classList.remove('hidden')); // 显示所有卡片
                activeCard = null;
            }
        });
    });
});
