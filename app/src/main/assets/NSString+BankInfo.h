

#import <Foundation/Foundation.h>

@interface NSString (BankInfo)


/**
 根据银行卡号

 @return 返回银行信息
 */
- (NSDictionary *)getBankInfo;

/**
 根据银行卡号
 
 @return 返回银行名称
 */
- (NSString *)getBankName;

/**
 根据银行卡号
 
 @return 返回银行卡类型
 */
- (NSString *)getBankcardTypeDescription;


@end
