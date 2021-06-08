stress = load('Cycstress.out');
strain = load('Cycstrain.out');
pwp = load('Cycpress.out');


figure()
subplot(2,2,1)
plot(strain(:,4) * 100, stress(:,4), 'k', 'linewidth', 1.25)
xlim([-3 3])
grid on
box on
xlabel('\gamma(%)')
ylabel('\tau(kPa)')
set(gca,'FontSize',10)

subplot(2,2,2)
plot(-stress(:,3), stress(:,4), 'k', 'linewidth', 1.25)
grid on
box on
xlabel('\sigma_v''(kPa)')
xlim([0 101])
ylabel('\tau(kPa)')
set(gca,'FontSize',10)

subplot(2,2,3)
plot(strain(:,4) * 100, pwp(:,2), 'k', 'linewidth', 1.25)
legend(['pwp from new' 10 'force-controlled driver'], 'Location', 'South')
xlim([-3 3])
ylim([0 101.3])
grid on
box on
xlabel('\gamma(%)')
ylabel('pwp(kPa)')
set(gca,'FontSize',10)

subplot(2,2,4)
plot(strain(:,4) * 100, -pwp(:,2) / stress(1,3),'linewidth', 1.25)
hold on
plot(strain(:,4) * 100, -pwp(:,2) / (0.75 * stress(1,3)), 'linewidth', 1.25)
plot(strain(:,4) * 100, 1 - stress(:,3) / stress(1,3),'--' , 'linewidth', 1.25)
legend('pwp / \sigma_{v0}', 'pwp / p_0', '1 - \sigma_v / \sigma_{v0}', 'Location', 'South')
xlim([-3 3])
grid on
box on
xlabel('\gamma(%)')
ylabel('Ru')
set(gca,'FontSize',10)

set(gcf,'paperposition',[0 0 8.0 6.0]);
print(gcf,'-djpeg','-r300','PM4Sand_wiki.jpg')

