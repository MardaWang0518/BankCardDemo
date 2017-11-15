package com.card.mardawang.bankcarddemo;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

//根据银行卡号获取银行及银行卡类型
public class MainActivity extends AppCompatActivity {

    private EditText et_cardnum;
    private TextView tv_bankname;
    private TextView tv_cardtype;
    private String cardnum;
    private BankInfoBean bankinfobean;
    private Button btn_get;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initView();
    }

    private void initView() {
        et_cardnum = (EditText) findViewById(R.id.et_cardnum);
        tv_bankname = (TextView) findViewById(R.id.tv_bankname);
        tv_cardtype = (TextView) findViewById(R.id.tv_cardtype);
        btn_get = (Button) findViewById(R.id.tv_get);


        btn_get.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                cardnum = et_cardnum.getText().toString().trim();
                if (cardnum!=null && checkBankCard(cardnum)) {
                    bankinfobean = new BankInfoBean(cardnum);
                    tv_bankname.setText(bankinfobean.getBankName());
                    tv_cardtype.setText(bankinfobean.getCardType());
                } else {
                    Toast.makeText(MainActivity.this, "卡号 "+cardnum+" is NOT valid", Toast.LENGTH_SHORT).show();
                }
            }
        });

    }

    /**
     * luhm校验
     * 从卡号最后一位数字开始，逆向将奇数位相加
     * 从卡号最后一位数字开始，逆向将偶数位数字，先乘以2（如果乘积为两位数，则将其减去9），再求和
     * 奇偶相加为10的倍数表示通过
     */
    private boolean validateluhm(String bankCode){
        //验证
        if(!bankCode.matches("^\\d{16,19}$")){
            throw new IllegalArgumentException("bankCode must be 16-19 number,bankCode is : "+bankCode);
        }
        //倒转
        String reverseCode = new StringBuffer(bankCode).reverse().toString();
        char[] array = reverseCode.toCharArray();
        int sumOdd = 0;
        int sumEven = 0;
        for(int i = 0;i<reverseCode.length();i++){
            int num = Integer.parseInt(String.valueOf(array[i]));
            if(i % 2 == 0){ //奇数位
                sumEven += num;
            }else{ //偶数位
                num = num * 2;
                if(num > 9){
                    num = num - 9;
                }
                sumOdd += num;
            }
        }
        if((sumOdd + sumEven) % 10 == 0){
            return true;
        }
        return false;
    }

    /**校验过程：
        1、从卡号最后一位数字开始，逆向将奇数位(1、3、5等等)相加。
        2、从卡号最后一位数字开始，逆向将偶数位数字，先乘以2（如果乘积为两位数，将个位十位数字相加，即将其减去9），再求和。
        3、将奇数位总和加上偶数位总和，结果应该可以被10整除。
     * 校验银行卡卡号
     */
    public static boolean checkBankCard(String bankCard) {
        if(bankCard.length() < 15 || bankCard.length() > 19) {
            return false;
        }
        char bit = getBankCardCheckCode(bankCard.substring(0, bankCard.length() - 1));
        if(bit == 'N'){
            return false;
        }
        return bankCard.charAt(bankCard.length() - 1) == bit;
    }

    /**
     * 从不含校验位的银行卡卡号采用 Luhm 校验算法获得校验位
     * @param nonCheckCodeBankCard
     * @return
     */
    public static char getBankCardCheckCode(String nonCheckCodeBankCard){
        if(nonCheckCodeBankCard == null || nonCheckCodeBankCard.trim().length() == 0
                || !nonCheckCodeBankCard.matches("\\d+")) {
            //如果传的不是数据返回N
            return 'N';
        }
        char[] chs = nonCheckCodeBankCard.trim().toCharArray();
        int luhmSum = 0;
        for(int i = chs.length - 1, j = 0; i >= 0; i--, j++) {
            int k = chs[i] - '0';
            if(j % 2 == 0) {
                k *= 2;
                k = k / 10 + k % 10;
            }
            luhmSum += k;
        }
        return (luhmSum % 10 == 0) ? '0' : (char)((10 - luhmSum % 10) + '0');
    }
}
