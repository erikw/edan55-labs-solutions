
r0 = [
4, 2.079442,
30, 9.864383,
40, 11.971350,
50, 13.870857,
];


r1 = [
4, 1.791759,
30, 4.795791,
40, 7.274480,
50, 8.649799,
60, 10.403839,
70, 11.827722,
80, 13.262157,
90, 14.477938,
];

r2 = [
4, 1.098612,
30, 3.496508,
40, 5.375278,
50, 6.982863,
60, 8.706656,
70, 9.991224,
80, 11.375375,
90, 12.477724,
100, 13.826046,
];

p0 = polyfit(r0(:,1), r0(:,2), 1);
c0 = exp(p0(1));
printf('c0=%f\n', c0)

p1 = polyfit(r1(:,1), r1(:,2), 1);
c1 = exp(p1(1));
printf('c1=%f\n', c1)

p2 = polyfit(r2(:,1), r2(:,2), 1);
c2 = exp(p2(1));
printf('c2=%f\n', c2)
